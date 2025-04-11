# map_config.py

from matplotlib.colors import ListedColormap

tile_colors = [
    "#dddddd", "#000000", "#ff9999", "#66ccff", "#ffcc00", "#00cc66", "#cc00ff",
    "#9999ff", "#ff66cc", "#ff6600", "#aaffaa", "#e6ccff", "#ffaa00", "#ffeecc",
    "#ff88aa", "#66ff66", "#ff4488", "#6688ff", "#ccff99", "#ffccff", "#ccaa00",
    "#0099cc", "#ffbbbb", "#99cc99", "#999999", "#cceeff", "#ccffcc", "#ff00ff",
    "#99e6ff", "#ffcc66",
]

tile_legend_labels = {
    0: "Corridor", 1: "Wall", 2: "Chairman's Office", 3: "Meeting Room 603",
    4: "RD_1", 5: "RD_2", 6: "RD_3", 7: "RD_4", 8: "Meeting Room 602",
    9: "Server Room", 10: "Pantry", 11: "Restroom", 12: "Classroom",
    13: "Meeting Room 601", 14: "Access Control 1", 15: "Access Control 2",
    16: "RD_5", 17: "RD_6", 18: "RD_7", 19: "RD_8", 20: "RD_9", 21: "RD_10",
    22: "RD_11", 23: "RD_12", 24: "RD_13", 25: "RD_14", 26: "Elevator 1",
    27: "Elevator 2", 28: "Elevator 3", 29: "Bin"
}

node_info_list = [
    {"nodeID": 0, "nodeName": "Corridor", "description": ""},
    {"nodeID": 1, "nodeName": "Wall", "description": ""},
    {"nodeID": 2, "nodeName": "Chairman's Office", "description": ""},
    {"nodeID": 3, "nodeName": "Meeting Room 603", "description": ""},
    {"nodeID": 4, "nodeName": "RD_1", "description": "Management Information System and Computer Device Engineer who provides technical support and maintenance for computer systems and devices."},
    {"nodeID": 5, "nodeName": "RD_2", "description": "Management Information System and Computer Device Engineer"},
    {"nodeID": 6, "nodeName": "RD_3", "description": "Management Information System and Computer Device Engineer"},
    {"nodeID": 7, "nodeName": "RD_4", "description": "Management Information System and Computer Device Engineer"},
    {"nodeID": 8, "nodeName": "Meeting Room 602", "description": ""},
    {"nodeID": 9, "nodeName": "Server Room", "description": "A server room is a room, usually air-conditioned, devoted to the continuous operation of computer servers."},
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
    {"nodeID": 22, "nodeName": "RD_11", "description": "In charge of APP and AIOT software developme"},
    {"nodeID": 23, "nodeName": "RD_12", "description": "AIOT team member"},
    {"nodeID": 24, "nodeName": "RD_13", "description": ""},
    {"nodeID": 25, "nodeName": "RD_14", "description": ""},
    {"nodeID": 26, "nodeName": "Elevator 1", "description": ""},
    {"nodeID": 27, "nodeName": "Elevator 2", "description": ""},
    {"nodeID": 28, "nodeName": "Elevator 3", "description": ""},
    {"nodeID": 29, "nodeName": "Bin", "description": ""},
]

tile_colormap = ListedColormap(tile_colors)

map_grid = [
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

passable_node_ids = [14, 15, 26, 27, 28]  # 可通行節點
