from django.test import TestCase
from process_runes import calculate_efficiency

# Create your tests here.
test_runes = {
    {
        "rune_id": 41638049729,
        "wizard_id": 35900893,
        "occupied_type": 2,
        "occupied_id": 0,
        "slot_no": 4,
        "rank": 15,
        "class": 16,
        "set_id": 4,
        "upgrade_limit": 15,
        "upgrade_curr": 12,
        "base_value": 445068,
        "sell_value": 67705,
        "pri_eff": [
        4,
        47
        ],
        "prefix_eff": [
        0,
        0
        ],
        "sec_eff": [
        [
            10,
            9,
            0,
            0
        ],
        [
            12,
            12,
            0,
            0
        ],
        [
            8,
            16,
            0,
            0
        ],
        [
            11,
            15,
            0,
            0
        ]
        ],
        "extra": 15
    },
    {
        "rune_id": 51313061664,
        "wizard_id": 35900893,
        "occupied_type": 2,
        "occupied_id": 0,
        "slot_no": 4,
        "rank": 5,
        "class": 6,
        "set_id": 4,
        "upgrade_limit": 15,
        "upgrade_curr": 12,
        "base_value": 427950,
        "sell_value": 66486,
        "pri_eff": [
        9,
        43
        ],
        "prefix_eff": [
        6,
        6
        ],
        "sec_eff": [
        [
            8,
            6,
            0,
            0
        ],
        [
            11,
            13,
            0,
            0
        ],
        [
            10,
            18,
            0,
            0
        ],
        [
            2,
            7,
            0,
            0
        ]
        ],
        "extra": 4
    },
    {
        "rune_id": 51813265082,
        "wizard_id": 35900893,
        "occupied_type": 2,
        "occupied_id": 0,
        "slot_no": 4,
        "rank": 4,
        "class": 6,
        "set_id": 4,
        "upgrade_limit": 15,
        "upgrade_curr": 9,
        "base_value": 313830,
        "sell_value": 33556,
        "pri_eff": [
        9,
        34
        ],
        "prefix_eff": [
        3,
        16
        ],
        "sec_eff": [
        [
            4,
            28,
            0,
            0
        ],
        [
            12,
            8,
            0,
            0
        ],
        [
            8,
            4,
            0,
            0
        ]
        ],
        "extra": 4
    },
}

print(calculate_efficiency(test_runes))