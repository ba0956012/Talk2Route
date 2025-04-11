import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import openai
from dotenv import load_dotenv
from openai import AzureOpenAI
import os
import json

load_dotenv()


AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_CHATGPT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHATGPT_DEPLOYMENT")
AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_OPENAI_EMB_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMB_DEPLOYMENT")


colors = [
    "#dddddd",  # 0: 空地（淺灰）
    "#000000",  # 1: 牆（黑）
    "#ff9999",  # 2
    "#66ccff",  # 3
    "#ffcc00",  # 4
    "#00cc66",  # 5
    "#cc00ff",  # 6
    "#9999ff",  # 7
    "#ff66cc",  # 8
    "#ff6600",  # 9
    "#aaffaa",  # 10
    "#e6ccff",  # 11
    "#ffaa00",  # 12
    "#ffeecc",  # 13
    "#ff88aa",  # 14
    "#66ff66",  # 15
    "#ff4488",  # 16
    "#6688ff",  # 17
    "#ccff99",  # 18
    "#ffccff",  # 19
    "#ccaa00",  # 20
    "#0099cc",  # 21
    "#ffbbbb",  # 22
    "#99cc99",  # 23
    "#999999",  # 24
    "#cceeff",  # 25
    "#ccffcc",  # 26
    "#ff00ff",  # 27
    "#99e6ff",  # 28
    "#ffcc66",  # 29
]

legend_labels = {
    0: "Corridor",
    1: "Wall",
    2: "Chairman's Office",
    3: "Meeting Room 603",
    4: "RD_1",
    5: "RD_2",
    6: "RD_3",
    7: "RD_4",
    8: "Meeting Room 602",
    9: "Server Room",
    10: "Pantry",
    11: "Restroom",
    12: "Classroom",
    13: "Meeting Room 601",
    14: "Access Control 1",
    15: "Access Control 2",
    16: "RD_5",
    17: "RD_6",
    18: "RD_7",
    19: "RD_8",
    20: "RD_9",
    21: "RD_10",
    22: "RD_11",
    23: "RD_12",
    24: "RD_13",
    25: "RD_14",
    26: "Elevator 1",
    27: "Elevator 2",
    28: "Elevator 3",
    29: "Bin",
}

MAP_INFO = [
    {"nodeID": 0, "nodeName": "Corridor", "description": ""},
    {"nodeID": 1, "nodeName": "Wall", "description": ""},
    {"nodeID": 2, "nodeName": "Chairman's Office", "description": ""},
    {"nodeID": 3, "nodeName": "Meeting Room 603", "description": ""},
    {
        "nodeID": 4,
        "nodeName": "RD_1",
        "description": "Management Information System and Computer Device Engineer who provides technical support and maintenance for computer systems and devices.",
    },
    {
        "nodeID": 5,
        "nodeName": "RD_2",
        "description": "Management Information System and Computer Device Engineer",
    },
    {
        "nodeID": 6,
        "nodeName": "RD_3",
        "description": "Management Information System and Computer Device Engineer",
    },
    {
        "nodeID": 7,
        "nodeName": "RD_4",
        "description": "Management Information System and Computer Device Engineer",
    },
    {"nodeID": 8, "nodeName": "Meeting Room 602", "description": ""},
    {
        "nodeID": 9,
        "nodeName": "Server Room",
        "description": "A server room is a room, usually air-conditioned, devoted to the continuous operation of computer servers.",
    },
    {"nodeID": 10, "nodeName": "Pantry", "description": ""},
    {"nodeID": 11, "nodeName": "Restroom", "description": ""},
    {"nodeID": 12, "nodeName": "Classroom", "description": ""},
    {"nodeID": 13, "nodeName": "Meeting Room 601", "description": ""},
    {"nodeID": 14, "nodeName": "Access Control 1", "description": ""},
    {"nodeID": 15, "nodeName": "Access Control 2", "description": ""},
    {"nodeID": 16, "nodeName": "RD_5", "description": ""},
    {"nodeID": 17, "nodeName": "RD_6", "description": ""},
    {"nodeID": 18, "nodeName": "RD_7", "description": ""},
    {"nodeID": 19, "nodeName": "RD_8", "description": ""},
    {"nodeID": 20, "nodeName": "RD_9", "description": ""},
    {"nodeID": 21, "nodeName": "RD_10", "description": ""},
    {
        "nodeID": 22,
        "nodeName": "RD_11",
        "description": "In charge of APP and AIOT software developme",
    },
    {"nodeID": 23, "nodeName": "RD_12", "description": "AIOT team member"},
    {"nodeID": 24, "nodeName": "RD_13", "description": ""},
    {"nodeID": 25, "nodeName": "RD_14", "description": ""},
    {"nodeID": 26, "nodeName": "Elevator 1", "description": ""},
    {"nodeID": 27, "nodeName": "Elevator 2", "description": ""},
    {"nodeID": 28, "nodeName": "Elevator 3", "description": ""},
    {"nodeID": 29, "nodeName": "Bin", "description": ""},
]


cmap = ListedColormap(colors)

# 地圖
room = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 24, 24, 24, 0, 25, 25, 25, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 24, 24, 24, 0, 25, 25, 25, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 22, 22, 22, 0, 23, 23, 23, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 22, 22, 22, 0, 23, 23, 23, 0, 1, 1, 1, 1, 1, 1, 1, 1, 12, 0, 0, 0, 15, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 20, 20, 20, 0, 21, 21, 21, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 27, 0],
    [0, 20, 20, 20, 0, 21, 21, 21, 0, 1, 1, 1, 1, 1, 1, 1, 1, 10, 0, 11, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 18, 18, 18, 0, 19, 19, 19, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 29, 0, 0, 0, 26],
    [0, 18, 18, 18, 0, 19, 19, 19, 0, 8, 8, 8, 1, 1, 1, 9, 1, 1, 0, 1, 1, 14, 0, 28, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 16, 16, 16, 0, 17, 17, 17, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 13, 1, 1, 1],
    [0, 16, 16, 16, 0, 17, 17, 17, 0, 0, 4, 4, 0, 6, 6, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 0, 5, 5, 0, 7, 7, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

PASS_NODE = [26, 27, 28, 14, 15]  # 可通行的節點


def find_positions(grid, target):
    return [
        (i, j)
        for i, row in enumerate(grid)
        for j, val in enumerate(row)
        if val == target
    ]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    start_val = grid[start[0]][start[1]]
    goal_val = grid[goal[0]][goal[1]]

    while not frontier.empty():
        _, current = frontier.get()
        if current == goal:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next = (current[0] + dx, current[1] + dy)
            if (
                0 <= next[0] < rows
                and 0 <= next[1] < cols
                and grid[next[0]][next[1]] in [0, start_val, goal_val] + PASS_NODE
            ):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current

    if goal not in came_from:
        return None
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = came_from[curr]
    path.append(start)
    path.reverse()
    return path


def draw_grid_with_legend(grid, path=None, show_text=False):
    grid_np = np.array(grid)
    plt.figure(figsize=(14, 9))
    ax = plt.gca()
    im = ax.imshow(grid_np, cmap=cmap, interpolation="none")

    if path:
        y, x = zip(*path)
        ax.plot(x, y, color="red", linewidth=2, marker="o")

    if show_text:
        for i in range(grid_np.shape[0]):
            for j in range(grid_np.shape[1]):
                ax.text(
                    j,
                    i,
                    str(grid_np[i, j]),
                    ha="center",
                    va="center",
                    fontsize=6,
                    color="black",
                )

    # plt.gca().invert_yaxis()
    plt.grid(True, which="both", color="gray", linestyle="--", linewidth=0.5)
    plt.xticks(range(grid_np.shape[1]))
    plt.yticks(range(grid_np.shape[0]))
    plt.title("Map and Path", fontsize=14)

    # 建立圖例 patch
    legend_elements = [
        Patch(facecolor=colors[val], edgecolor="black", label=f"{val}: {desc}")
        for val, desc in legend_labels.items()
    ]

    # 放在圖下方
    plt.legend(
        handles=legend_elements,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.08),
        ncol=4,
        fontsize=10,
        frameon=False,
    )

    plt.tight_layout()
    plt.show()


def generate_prompt(user_input, map_nodes):
    """
    根據使用者輸入與地圖節點資料產生 prompt 字串，用於 Azure OpenAI。

    Args:
        user_input (str): 使用者輸入的訊息。
        map_nodes (list[dict]): 地圖節點資料，每個節點為一個 dict，包含 nodeID、nodeName、description。

    Returns:
        str: 要給 OpenAI 的完整 prompt。
    """

    system_prompt = "你是一個地圖導引助手。根據使用者輸入的內容，從下列節點資訊中，找出一個最合適的目的地，只回傳那一筆節點的 JSON："

    nodes_info = "\n".join(
        [
            f"{node['nodeID']}: {node['nodeName']} - {node['description']}"
            for node in map_nodes
        ]
    )

    final_prompt = f"""{system_prompt}

    地圖節點：
    {nodes_info}

    使用者輸入：
    「{user_input}」

    請回傳一筆最適合的節點資料（JSON 格式），例如：
    {{"nodeID": 0, "nodeName": "Corridor", "description": ""}}"""

    return final_prompt


if __name__ == "__main__":
    start_val = int(input("請輸入起點數字："))
    query = input("query: ")

    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
    )

    generate_prompt = generate_prompt(query, MAP_INFO)

    response = response = client.chat.completions.create(
        model=AZURE_OPENAI_CHATGPT_DEPLOYMENT,  # 或你設的部署名稱
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "你是一個地圖導引助手，請根據使用者輸入選出最合適的節點",
            },
            {"role": "user", "content": generate_prompt},
        ],
        temperature=0,
        top_p=1,
        max_tokens=200,
    )
    print(response.choices[0].message.content)

    response_json = json.loads(response.choices[0].message.content)
    end_val = response_json.get("nodeID", 0)

    start_points = find_positions(room, start_val)
    end_points = find_positions(room, end_val)

    start = start_points[0]
    goal = end_points[0]

    path = astar(room, start, goal)

    if path:
        print("找到路徑，共 {} 步：".format(len(path) - 1))  # 不含起點

        direction_map = {(-1, 0): "上", (1, 0): "下", (0, -1): "左", (0, 1): "右"}

        last_dir = None
        count = 0
        segment_start = path[0]

        path_text = ""

        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            dy = curr[0] - prev[0]
            dx = curr[1] - prev[1]
            current_dir = (dy, dx)

            if current_dir == last_dir:
                count += 1
            else:
                if last_dir is not None:
                    direction_str = direction_map.get(last_dir, "未知方向")
                    path_text += f"往{direction_str}走 {count} 步 \n"
                segment_start = prev
                count = 1
                last_dir = current_dir

        # 最後一段也印出來
        if last_dir is not None:
            direction_str = direction_map.get(last_dir, "未知方向")
            path_text += f"往{direction_str}走 {count} 步 \n"
            # print(f"{segment_start} → {path[-1]}：{direction_str} x{count}")
    else:
        print("找不到路徑")

    print(f'目的地是{response_json["nodeName"]}')
    print(path_text)

    draw_grid_with_legend(room, path, show_text=True)
