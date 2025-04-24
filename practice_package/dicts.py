
import copy


def count_char_occurrences(text):
    from collections import Counter
    filtered = [ch.lower() for ch in text if ch.isalpha()]
    return dict(Counter(filtered))


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for k, v2 in dict2.items():
        if k in result:
            v1 = result[k]
            result[k] = conflict_resolver(k, v1, v2)
        else:
            result[k] = v2
    return result


def invert_dictionary(original_dict):
    inverted = {}
    for k, v in original_dict.items():
        if v in inverted:
            inverted[v].append(k)
        else:
            inverted[v] = [k]
    return inverted


def dict_to_table(data_dict, columns):
    headers = [col.upper() for col in columns]
    rows = []
    for key in data_dict:
        row = []
        for col in columns:
            val = data_dict[key].get(col, "N/A")
            row.append(str(val))
        rows.append(row)

    col_widths = [
        max(
            len(headers[i]),
            max(len(row[i]) for row in rows)
        ) if rows else len(headers[i])
        for i in range(len(columns))
    ]

    lines = []
    header_line = (
        "| "
        + " | ".join(
            headers[i].ljust(col_widths[i]) for i in range(len(columns))
        )
        + " |"
    )
    lines.append(header_line)
    separator_line = (
        "|"
        + "|".join(
            "-" * (col_widths[i] + 2) for i in range(len(columns))
        )
        + "|"
    )
    lines.append(separator_line)
    for row in rows:
        line = (
            "| "
            + " | ".join(
                row[i].ljust(col_widths[i]) for i in range(len(columns))
            )
            + " |"
        )
        lines.append(line)
    return "\n".join(lines)


def deep_update(base_dict, update_dict):
    result = copy.deepcopy(base_dict)
    for k, v in update_dict.items():
        if k in result:
            if isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = deep_update(result[k], v)
            else:
                result[k] = v
        else:
            result[k] = v
    return result
