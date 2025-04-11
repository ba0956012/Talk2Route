from map_config import map_grid, node_info_list, tile_colormap, tile_colors, tile_legend_labels, passable_node_ids
from astar import astar, find_positions
from visualization import draw_grid_with_legend
from openai_helper import get_destination_node

if __name__ == "__main__":
    start_val = int(input("請輸入起點數字："))
    query = input("query: ")

    try:
        response_json = get_destination_node(query, node_info_list)
        end_val = response_json["nodeID"]
    except Exception as e:
        print("無法取得目的地，請確認 API 回應或節點資料是否正確。")
        raise e

    start_points = find_positions(map_grid, start_val)
    end_points = find_positions(map_grid, end_val)

    start = start_points[0]
    goal = end_points[0]

    path = astar(map_grid, start, goal, passable_node_ids)

    if path:
        print("找到路徑，共 {} 步：".format(len(path) - 1))
        direction_map = {(-1, 0): "上", (1, 0): "下", (0, -1): "左", (0, 1): "右"}
        path_text = ""
        last_dir = None
        count = 0

        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            dy, dx = curr[0] - prev[0], curr[1] - prev[1]
            current_dir = (dy, dx)
            if current_dir == last_dir:
                count += 1
            else:
                if last_dir is not None:
                    path_text += f"往{direction_map.get(last_dir, '未知方向')}走 {count} 步\n"
                last_dir = current_dir
                count = 1
        if last_dir is not None:
            path_text += f"往{direction_map.get(last_dir, '未知方向')}走 {count} 步\n"
        print(f"目的地是 {response_json['nodeName']}")
        print(path_text)
    else:
        print("找不到路徑")

    draw_grid_with_legend(map_grid, path, show_text=True, cmap=tile_colormap, colors=tile_colors, legend_labels=tile_legend_labels)
