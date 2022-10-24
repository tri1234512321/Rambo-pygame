level_map = [
    "                                                                                                                                                                                                        ",
    "                                                                                                                                                                                                        ",
    "                                                                                         C  C  C  C  C                                                                        C  C          CCCC        ",
    "                 CCC      CCC                                        LXXXXXR             C  C  C  C  C                                                                        C  C        LXXXXXXR      ",
    "                 CCC      CCC                                                            C  C  C  C  C  LXXXXXXXXXR                                                           C  C                      ",
    "                 CCC      CCC                       LXXXXXXXXXXXXXR          LXXXXXXXXR  C  C  C  C  C                                                                        C  C                      ",
    "              LXXXXXXR  LXXXXXXXXR                                                       T  T  T  T  T                                                            LXXXXXXXXR  T  T  LXXR            LXXR",
    "                                                                                         O  O  O  O  O               LXXXXXXXXXXR                    LXXXXXXXXXR              O  O                      ",
    "LXXXXXXXXXXR                        LXXXXXXXXXXXXR                                       O  O  O  O  O                                                                        O  O                      ",
    "                                                                                         B  B  B  B  B                             LXXXXXXXXXXXXXXXR                          B  B      LXXXXXXXXXXR    ",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
# LXR is horizontal land
# T
# O is stone column
# B
# C is coin
# W is water

tile_size = 64

SCREEN_WIDTH = 1200
SCREEN_hEIGHT = tile_size * len(level_map)
