import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import math

print("=" * 70)
print("                    DFA TO NFA CONVERSION")
print("=" * 70)

print("\nProblem Statement:")
print("Construct a DFA and an equivalent NFA over {0,1}")
print("that accepts all strings containing 01 OR 11 as a substring.")

states = ["A", "B", "C", "D"]
alphabet = {"0", "1"}
start_state = "A"
dfa_final_states = {"D"}

dfa = {
    "A": {
        "0": "B",
        "1": "C"
    },
    "B": {
        "0": "B",
        "1": "D"
    },
    "C": {
        "0": "B",
        "1": "D"
    },
    "D": {
        "0": "D",
        "1": "D"
    }
}

print("\n" + "=" * 70)
print("                    DFA TRANSITIONS")
print("=" * 70)

print(f"{'STATE':<10}{'0':<10}{'1':<10}")
print("-" * 30)

for state in states:
    print(
        f"{state:<10}"
        f"{dfa[state]['0']:<10}"
        f"{dfa[state]['1']:<10}"
    )

print("\nDFA Start State:", start_state)
print("DFA Final State:", ", ".join(dfa_final_states))

nfa_states = states + ["F"]

nfa = {}

for state in states:
    nfa[state] = {
        "0": {dfa[state]["0"]},
        "1": {dfa[state]["1"]},
        "ε": set()
    }

nfa["D"]["ε"] = {"F"}

nfa["F"] = {
    "0": set(),
    "1": set(),
    "ε": set()
}

nfa_final_states = {"F"}

print("\n" + "=" * 70)
print("                    EQUIVALENT NFA")
print("=" * 70)

print(f"{'STATE':<10}{'0':<15}{'1':<15}{'ε':<15}")
print("-" * 55)

for state in nfa_states:

    zero = ", ".join(sorted(nfa[state]["0"])) if nfa[state]["0"] else "-"
    one = ", ".join(sorted(nfa[state]["1"])) if nfa[state]["1"] else "-"
    epsilon = ", ".join(sorted(nfa[state]["ε"])) if nfa[state]["ε"] else "-"

    print(
        f"{state:<10}"
        f"{zero:<15}"
        f"{one:<15}"
        f"{epsilon:<15}"
    )

print("\nNFA Start State:", start_state)
print("NFA Final State:", ", ".join(nfa_final_states))


def draw_state(ax, x, y, name, final=False):

    circle = Circle(
        (x, y),
        0.55,
        fill=False,
        linewidth=2.5
    )

    ax.add_patch(circle)

    if final:
        inner = Circle(
            (x, y),
            0.43,
            fill=False,
            linewidth=2
        )

        ax.add_patch(inner)

    ax.text(
        x,
        y,
        name,
        fontsize=16,
        fontweight="bold",
        ha="center",
        va="center"
    )


def draw_start_arrow(ax, x, y):

    ax.annotate(
        "",
        xy=(x - 0.55, y),
        xytext=(x - 1.5, y),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2.5
        )
    )


def draw_arrow(ax, x1, y1, x2, y2, label, curve=0):

    arrow = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="->",
        mutation_scale=18,
        linewidth=2,
        connectionstyle=f"arc3,rad={curve}"
    )

    ax.add_patch(arrow)

    dx = x2 - x1
    dy = y2 - y1

    length = math.sqrt(dx * dx + dy * dy)

    if length != 0:
        ox = -dy / length * 0.25
        oy = dx / length * 0.25
    else:
        ox = 0
        oy = 0

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    ax.text(
        mx + ox,
        my + oy,
        label,
        fontsize=13,
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            pad=2
        )
    )


def draw_loop(ax, x, y, label):

    arrow = FancyArrowPatch(
        (x + 0.35, y + 0.35),
        (x + 0.35, y - 0.35),
        arrowstyle="->",
        mutation_scale=18,
        linewidth=2,
        connectionstyle="arc3,rad=-1.8"
    )

    ax.add_patch(arrow)

    ax.text(
        x + 0.85,
        y,
        label,
        fontsize=13,
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(
            facecolor="white",
            edgecolor="none"
        )
    )


def create_nfa_diagram():

    fig, ax = plt.subplots(figsize=(16, 9))

    ax.set_xlim(-7, 7)
    ax.set_ylim(-5, 5)
    ax.axis("off")

    ax.text(
        0,
        4.4,
        "DFA → NFA Conversion",
        fontsize=25,
        fontweight="bold",
        ha="center"
    )

    ax.text(
        0,
        3.9,
        "Equivalent NFA with ε-transition",
        fontsize=14,
        ha="center"
    )

    positions = {
        "A": (-5, 0),
        "B": (-2, 2.5),
        "C": (-2, -2.5),
        "D": (1.5, 0),
        "F": (5, 0)
    }

    for state in nfa_states:

        x, y = positions[state]

        draw_state(
            ax,
            x,
            y,
            state,
            final=state in nfa_final_states
        )

    draw_start_arrow(
        ax,
        positions["A"][0],
        positions["A"][1]
    )

    draw_arrow(
        ax,
        -4.5,
        0,
        -2.5,
        2.2,
        "0"
    )

    draw_arrow(
        ax,
        -4.5,
        0,
        -2.5,
        -2.2,
        "1"
    )

    draw_loop(
        ax,
        -2,
        2.5,
        "0"
    )

    draw_arrow(
        ax,
        -1.5,
        2.3,
        1.0,
        0.3,
        "1"
    )

    draw_arrow(
        ax,
        -2,
        -2.0,
        -2,
        2.0,
        "0",
        curve=0.2
    )

    draw_arrow(
        ax,
        -1.5,
        -2.3,
        1.0,
        -0.3,
        "1"
    )

    draw_loop(
        ax,
        1.5,
        0,
        "0,1"
    )

    draw_arrow(
        ax,
        2.1,
        0,
        4.4,
        0,
        "ε"
    )

    ax.text(
        -5.5,
        -4.3,
        "→ Initial State",
        fontsize=12
    )

    ax.text(
        -1,
        -4.3,
        "Double Circle = Final State",
        fontsize=12
    )

    ax.text(
        3,
        -4.3,
        "ε = Empty String Transition",
        fontsize=12
    )

    output = r"C:\Assignment ACD\DFA to NFA\dfa_to_nfa_diagram.png"

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nNFA diagram saved at:")
    print(output)

    plt.show()


def create_state_mapping():

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.axis("off")

    rows = [
        ["A", "A", "No"],
        ["B", "B", "No"],
        ["C", "C", "No"],
        ["D", "D", "No"],
        ["New State", "F", "Yes"]
    ]

    table = ax.table(
        cellText=rows,
        colLabels=[
            "DFA State",
            "NFA State",
            "NFA Final?"
        ],
        cellLoc="center",
        loc="center",
        colWidths=[0.3, 0.3, 0.3]
    )

    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 2)

    ax.set_title(
        "DFA to NFA State Mapping",
        fontsize=20,
        fontweight="bold",
        pad=25
    )

    ax.text(
        0.5,
        0.08,
        "D → ε → F",
        fontsize=16,
        fontweight="bold",
        ha="center"
    )

    output = r"C:\Assignment ACD\DFA to NFA\dfa_to_nfa_state_mapping.png"

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nState mapping saved at:")
    print(output)

    plt.show()


create_nfa_diagram()
create_state_mapping()

print("\n" + "=" * 70)
print("                    CONVERSION COMPLETE")
print("=" * 70)