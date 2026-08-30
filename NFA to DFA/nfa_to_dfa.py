import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from collections import deque
import math

print("=" * 70)
print("                 ε-NFA TO DFA CONVERSION")
print("=" * 70)

print("\nProblem Statement:")
print("Construct an ε-NFA and an equivalent DFA over {0,1}")
print("that accepts all strings containing 01 OR 11 as a substring.")

nfa = {
    "q0": {
        "0": {"q0"},
        "1": {"q0"},
        "ε": {"q1", "q4"}
    },
    "q1": {
        "0": {"q2"},
        "1": set(),
        "ε": set()
    },
    "q2": {
        "0": set(),
        "1": {"q3"},
        "ε": set()
    },
    "q3": {
        "0": {"q3"},
        "1": {"q3"},
        "ε": set()
    },
    "q4": {
        "0": set(),
        "1": {"q5"},
        "ε": set()
    },
    "q5": {
        "0": set(),
        "1": {"q6"},
        "ε": set()
    },
    "q6": {
        "0": {"q6"},
        "1": {"q6"},
        "ε": set()
    }
}

alphabet = {"0", "1"}
start_state = "q0"
nfa_final_states = {"q3", "q6"}

def epsilon_closure(states):
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop()

        for next_state in nfa[state]["ε"]:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return frozenset(closure)

def move(states, symbol):
    result = set()

    for state in states:
        result.update(nfa[state][symbol])

    return result

print("\n" + "=" * 70)
print("                    ε-CLOSURES")
print("=" * 70)

for state in nfa:
    closure = epsilon_closure({state})

    print(
        f"ε-closure({state}) = "
        f"{{{', '.join(sorted(closure))}}}"
    )

dfa_start = epsilon_closure({start_state})
dfa_states = {dfa_start}
dfa_transitions = {}
queue = deque([dfa_start])

while queue:
    current = queue.popleft()
    dfa_transitions[current] = {}

    for symbol in sorted(alphabet):
        moved = move(current, symbol)
        destination = epsilon_closure(moved)

        dfa_transitions[current][symbol] = destination

        if destination not in dfa_states:
            dfa_states.add(destination)
            queue.append(destination)

dfa_final_states = set()

for state in dfa_states:
    if state.intersection(nfa_final_states):
        dfa_final_states.add(state)

dfa_states = sorted(
    dfa_states,
    key=lambda x: (
        len(x),
        sorted(x)
    )
)

state_names = {}

for i, state in enumerate(dfa_states):
    state_names[state] = chr(ord("A") + i)

print("\n" + "=" * 70)
print("                    DFA STATES")
print("=" * 70)

for state in dfa_states:
    name = state_names[state]
    subset = "{" + ", ".join(sorted(state)) + "}"

    if state in dfa_final_states:
        print(f"{name} = {subset}   <-- FINAL")
    else:
        print(f"{name} = {subset}")

print("\n" + "=" * 70)
print("                 DFA TRANSITION TABLE")
print("=" * 70)

print(
    f"{'STATE':<10}"
    f"{'0':<10}"
    f"{'1':<10}"
)

print("-" * 30)

for state in dfa_states:
    name = state_names[state]

    zero = state_names[dfa_transitions[state]["0"]]
    one = state_names[dfa_transitions[state]["1"]]

    print(
        f"{name:<10}"
        f"{zero:<10}"
        f"{one:<10}"
    )

print("\nStart State:", state_names[dfa_start])

print(
    "Final States:",
    ", ".join(
        state_names[s]
        for s in dfa_final_states
    )
)

def draw_state(ax, x, y, name, final=False):
    outer = Circle(
        (x, y),
        0.55,
        fill=False,
        linewidth=2.5
    )

    ax.add_patch(outer)

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
        xytext=(x - 1.4, y),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2.5
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
        offset_x = -dy / length * 0.25
        offset_y = dx / length * 0.25
    else:
        offset_x = 0
        offset_y = 0

    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2

    ax.text(
        middle_x + offset_x,
        middle_y + offset_y,
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

combined_transitions = {}

for state in dfa_states:
    source = state_names[state]

    for symbol in ["0", "1"]:
        destination = dfa_transitions[state][symbol]
        target = state_names[destination]
        key = (source, target)

        if key not in combined_transitions:
            combined_transitions[key] = []

        combined_transitions[key].append(symbol)

def create_dfa_diagram():
    fig, ax = plt.subplots(figsize=(16, 10))

    ax.set_xlim(-7, 7)
    ax.set_ylim(-5.5, 5.5)
    ax.axis("off")

    ax.text(
        0,
        5,
        "Equivalent DFA",
        fontsize=25,
        fontweight="bold",
        ha="center"
    )

    ax.text(
        0,
        4.5,
        "NFA → DFA using ε-Closure and Subset Construction",
        fontsize=13,
        ha="center"
    )

    positions = {
        "A": (-5, 0),
        "B": (-2.5, 2.8),
        "C": (-2.5, -2.8),
        "D": (0.5, 3.2),
        "F": (0.5, 0),
        "G": (0.5, -3.2),
        "E": (3.8, 3.2),
        "I": (3.8, 0),
        "H": (3.8, -3.2)
    }

    for state in dfa_states:
        name = state_names[state]
        x, y = positions[name]

        draw_state(
            ax,
            x,
            y,
            name,
            final=state in dfa_final_states
        )

    start_name = state_names[dfa_start]
    sx, sy = positions[start_name]

    draw_start_arrow(ax, sx, sy)

    for (source, target), symbols in combined_transitions.items():
        label = ",".join(symbols)

        x1, y1 = positions[source]
        x2, y2 = positions[target]

        if source == target:
            draw_loop(ax, x1, y1, label)

        else:
            curve = 0

            if source == "C" and target == "B":
                curve = 0.25
            elif source == "B" and target == "F":
                curve = -0.08
            elif source == "C" and target == "G":
                curve = -0.08
            elif source == "F" and target == "D":
                curve = 0.20
            elif source == "G" and target == "E":
                curve = 0.20
            elif source == "I" and target == "H":
                curve = 0.20
            elif source == "H" and target == "I":
                curve = -0.20

            draw_arrow(
                ax,
                x1,
                y1,
                x2,
                y2,
                label,
                curve
            )

    ax.text(
        -5.5,
        -4.6,
        "→ Initial State",
        fontsize=12
    )

    ax.text(
        -1,
        -4.6,
        "Double Circle = Final State",
        fontsize=12
    )

    ax.text(
        3,
        -4.6,
        "A–I = DFA States",
        fontsize=12
    )

    output = (
        r"C:\Assignment ACD\NFA to DFA"
        r"\converted_dfa_diagram.png"
    )

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nDFA diagram saved at:")
    print(output)

    plt.show()

def create_mapping_table():
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.axis("off")

    rows = []

    for state in dfa_states:
        name = state_names[state]

        subset = (
            "{"
            + ", ".join(sorted(state))
            + "}"
        )

        final = (
            "Yes"
            if state in dfa_final_states
            else "No"
        )

        rows.append([
            name,
            subset,
            final
        ])

    table = ax.table(
        cellText=rows,
        colLabels=[
            "DFA State",
            "ε-NFA State Subset",
            "Final State?"
        ],
        cellLoc="center",
        loc="center",
        colWidths=[
            0.20,
            0.55,
            0.20
        ]
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2)

    ax.set_title(
        "DFA State Mapping",
        fontsize=20,
        fontweight="bold",
        pad=25
    )

    output = (
        r"C:\Assignment ACD\NFA to DFA"
        r"\dfa_state_mapping.png"
    )

    plt.savefig(
        output,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nState mapping saved at:")
    print(output)

    plt.show()

create_dfa_diagram()
create_mapping_table()

print("\n" + "=" * 70)
print("                    CONVERSION COMPLETE")
print("=" * 70)