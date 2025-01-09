try:
    from manimlib import *

    manimce = False
except ImportError as e:
    from manim import *

    manimce = True
import colour

# Parsing parameters
YACV_ACTION = "ACTION"
YACV_ACCEPT = "ACC"
YACV_ERROR = "ERR"
YACV_GOTO = "GOTO"
YACV_DOT = "•"
YACV_REDUCE = "r"
YACV_SHIFT = "s"
YACV_EPSILON = ""

# Graphviz parameters
YACV_GRAPHVIZ_INFINITY = 2048
YACV_GRAPHVIZ_COLORS = [
    "#FF7F50",  # 'coral',
    "#8B008B",  # 'darkmagenta',
    "#006400",  # 'darkblue',
    "#8B0000",  # 'darkred',
    "#FF1493",  # 'deeppink',
    "#1E90FF",  # 'dodgerblue',
    "#8A2BE2",  # 'blueviolet',
    "#008B8B",  # 'darkcyan',
    "#FFFF00",  # 'yellow',
    "#191970",  # 'mediumslateblue',
    "#A52A2A",  # 'brown',
    "#FFA500",  # 'orange',
    "#008080",  # 'teal',
    "#2E8B57",  # 'seagreen',
    "#00FF7F",  # 'springgreen',
    "#FF6347",  # 'tomato'
]

# Manim parameters
YACV_MANIM_MAX_AST_WIDTH = 10
YACV_MANIM_MAX_AST_HEIGHT = 6.5
YACV_MANIM_MAX_STACK_VIS = 6
YACV_MANIM_TEXT_SCALE = 0.5
YACV_MANIM_STATUS_SCALE = 0.6
YACV_MANIM_STRING_SCALE = 0.5
YACV_MANIM_STRING_LEADER = "\\textbf{S'} $\\rightarrow$ \\textbf{[}" if manimce else "S' \\rightarrow ["

# Hackable config for manim
yacv_manimce_config = {
    "assets_dir": "./",
    "background_color": colour.Color("#000"),
    "background_opacity": 1.0,
    "custom_folders": False,
    "disable_caching": False,
    "ffmpeg_loglevel": "ERROR",
    "flush_cache": False,
    "frame_height": 8.0,
    "frame_rate": 15,
    "frame_width": 14.222222222222221,
    "from_animation_number": 0,
    "images_dir": "{media_dir}/images/{module_name}",
    "leave_progress_bars": False,
    "log_dir": "{media_dir}/logs",
    "log_to_file": False,
    "max_files_cached": 100,
    "media_dir": "./media",
    "movie_file_extension": ".mp4",
    "output_file": "ParsingVis",
    "partial_movie_dir": "{video_dir}/partial_movie_files/{scene_name}",
    "pixel_height": 720,
    "pixel_width": 1280,
    "plugins": [],
    "png_mode": "RGB",
    "preview": False,
    "progress_bar": True,
    "save_as_gif": False,
    "save_last_frame": False,
    "save_pngs": False,
    "scene_names": None,
    "show_in_file_browser": False,
    "sound": False,
    "tex_dir": "{media_dir}/Tex",
    "tex_template_file": None,
    "text_dir": "{media_dir}/texts",
    "upto_animation_number": float("inf"),
    "use_webgl_renderer": False,
    "verbosity": "INFO",
    "video_dir": "{media_dir}/videos/{module_name}/{quality}",
    "webgl_renderer_path": "",
    "webgl_updater_fps": 15,
    "write_all": False,
    "write_to_movie": True,
}
yacv_manim_config = {
    "camera_config": {
        "background_color": colour.Color("#000"),
        # "frame_rate": 60,
        # "pixel_height": 720,
        # "pixel_width": 1280,
    },
    # "end_at_animation_number": None,
    "file_writer_config": {
        "file_name": "ParsingVis",
        # "mirror_module_path": False,
        "movie_file_extension": ".mp4",
        "open_file_upon_completion": True,
        "png_mode": "RGB",
        # "quiet": False,
        "save_last_frame": False,
        # "save_pngs": False,
        "show_file_location_upon_completion": True,
        "write_to_movie": True,
    },
    "leave_progress_bars": True,
    # "preview": False,
    # "quiet": False,
    # "scene_names": None,
    "skip_animations": False,
    "start_at_animation_number": None,
    # "window_config": None,
    # "write_all": False,
}
