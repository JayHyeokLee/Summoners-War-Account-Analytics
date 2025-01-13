from .mapping import mapping

def calculate_efficiency(rune):
    #calculate current and maximum rune efficiency

    ratio = 0.0

     # Main stat efficiency
    main_stat = rune["pri_eff"][0]
    main_value = rune["pri_eff"][1]
    max_main = mapping["rune"]["effectTypes"]["main"][main_stat]["max"][rune["class"]]
    ratio += main_value / max_main

    # Sub stat efficiency
    for stat in rune["sec_eff"]:
        stat_type = stat[0]
        stat_value = stat[1] + stat[3]  # Base value + bonus
        max_sub = mapping["rune"]["effectTypes"]["sub"][stat_type]["max"][6]
        ratio += stat_value / max_sub

    # Prefix stat efficiency (innate stat)
    if rune.get("prefix_eff") and rune["prefix_eff"][0] > 0:
        prefix_stat = rune["prefix_eff"][0]
        prefix_value = rune["prefix_eff"][1]
        max_prefix = mapping["rune"]["effectTypes"]["sub"][prefix_stat]["max"][6]
        ratio += prefix_value / max_prefix

    # Efficiency calculations
    current_efficiency = (ratio / 2.8) * 100
    max_efficiency = current_efficiency + (
        (max(0, (12 - rune["upgrade_curr"]) // 3) * 0.2) / 2.8 * 100
    )

    return {
        "rune_id": rune["rune_id"],
        "current_efficiency": round(current_efficiency, 2),
        "max_efficiency": round(max_efficiency, 2),
    }