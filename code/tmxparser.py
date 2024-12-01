import xml.etree.ElementTree as ET
import base64
import zlib, struct
from game_data import *

class TMXParser:
    def __init__(self, tmx_file):
        self.tmx_file = tmx_file
        self.level_data = self.load_tmx_data()

    def normalize_data(self, grid, layer_name):
        # Tạo lưới mới với mọi giá trị khác -1 trừ đi số nhỏ nhất
        return [[val - layer_counts[layer_name] if val != -1 else -1 for val in row] for row in grid]


    def load_tmx_data(self):
        """Đọc và xử lý dữ liệu từ file .tmx."""
        # Đọc file .tmx
        tree = ET.parse(self.tmx_file)
        root = tree.getroot()

        # Lấy kích thước bản đồ
        width = int(root.attrib['width'])
        height = int(root.attrib['height'])

        # Dictionary để lưu trữ dữ liệu các layer
        level_data = {}

        # Duyệt qua các layer
        for layer in root.findall('layer'):
            layer_name = layer.attrib['name']
            data = layer.find('data').text.strip()

            # Giải mã dữ liệu nếu cần
            encoding = layer.find('data').attrib.get('encoding')
            compression = layer.find('data').attrib.get('compression')

            if encoding == "base64":
                decoded_data = base64.b64decode(data)
                if compression == "zlib":
                    decoded_data = zlib.decompress(decoded_data)

                # Chuyển dữ liệu thành danh sách số nguyên
                tile_ids = [struct.unpack('<I', decoded_data[i:i + 4])[0]
                    for i in range(0, len(decoded_data), 4)]

            else:
                raise ValueError("Unsupported encoding or compression")

            # Thay đổi tile ID để giống Tiled Map
            tile_ids = [-1 if tile_id == 0 else tile_id for tile_id in tile_ids]

            # Chuyển dữ liệu thành dạng lưới
            grid = [tile_ids[i:i + width] for i in range(0, len(tile_ids), width)]

            # Chuẩn hóa giá trị trong grid
            normalized_grid = self.normalize_data(grid, layer_name)
            

            # Lưu dữ liệu lưới vào dictionary
            level_data[layer_name] = normalized_grid

        return level_data
