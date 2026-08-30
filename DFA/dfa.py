import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

# PROBLEM STATEMENT

problem = """
Construct a DFA over {0,1} that accepts all strings
containing 01 OR 11 as a substring.
"""

# DRAW STATE

def draw_state(ax, x, y, name, final=False):

    circle = Circle(
        (x, y),
        0.45,
        fill=False,
        linewidth=2.5
    )

    ax.add_patch(circle)

    # Double circle for final state

    if final:

        inner = Circle(
            (x, y),
            0.36,
            fill=False,
            linewidth=2
        )

        ax.add_patch(inner)

    ax.text(
        x,
        y,
        name,
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold"
    )
def draw_arrow(
        ax,
        start,
        end,
        label,
        curve=0,
        label_offset=(0, 0)
):

    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="->",
        mutation_scale=18,
        linewidth=2,
        connectionstyle=f"arc3,rad={curve}"
    )

    ax.add_patch(arrow)

    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2

    ax.text(
        mid_x + label_offset[0],
        mid_y + label_offset[1],
        label,
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            pad=2
        )
    )

# DRAW SELF LOOP

def draw_self_loop(ax, x, y, label):

    arrow = FancyArrowPatch(
        (x + 0.30, y + 0.30),
        (x + 0.30, y - 0.30),
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
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            pad=2
        )
    )

# START ARROW

def draw_start_arrow(ax, x, y):

    ax.annotate(
        "",
        xy=(x - 0.45, y),
        xytext=(x - 1.2, y),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2.5
        )
    )

# CREATE DFA DIAGRAM

def create_dfa_diagram():

    fig, ax = plt.subplots(figsize=(15, 8))

    ax.set_xlim(-2, 12)
    ax.set_ylim(-4, 4)

    ax.axis("off")

    # TITLE


    ax.text(
        5,
        3.4,
        "DFA",
        fontsize=22,
        fontweight="bold",
        ha="center"
    )

    ax.text(
        5,
        2.9,
        "Strings containing 01 OR 11",
        fontsize=13,
        ha="center"
    )

    # STATE POSITIONS

    A = (0, 0)
    B = (3, 2)
    C = (3, -2)
    D = (8, 0)

    # DRAW STATES

    draw_state(ax, *A, "A")
    draw_state(ax, *B, "B")
    draw_state(ax, *C, "C")
    draw_state(ax, *D, "D", final=True)

    # INITIAL STATE
    
    draw_start_arrow(ax, *A)

    # A → B : 0

    draw_arrow(
        ax,
        (0.35, 0.25),
        (2.55, 1.75),
        "0",
        label_offset=(0, 0.15)
    )

  
    # A → C : 1

    draw_arrow(
        ax,
        (0.35, -0.25),
        (2.55, -1.75),
        "1",
        label_offset=(0, -0.15)
    )

    # B → B : 0

    draw_self_loop(
        ax,
        *B,
        "0"
    )

    # C → B : 0

    draw_arrow(
        ax,
        (3, -1.55),
        (3, 1.55),
        "0",
        curve=0.35,
        label_offset=(0.55, 0)
    )

    # B → D : 1
    
    draw_arrow(
        ax,
        (3.45, 1.75),
        (7.55, 0.35),
        "1",
        label_offset=(0, 0.2)
    )

    # C → D : 1

    draw_arrow(
        ax,
        (3.45, -1.75),
        (7.55, -0.35),
        "1",
        label_offset=(0, -0.2)
    )

    # D → D : 0,1
    
    draw_self_loop(
        ax,
        *D,
        "0, 1"
    )

    ax.text(
        1,
        -3.3,
        "→ Initial State",
        fontsize=11
    )

    ax.text(
        5,
        -3.3,
        "Double Circle = Final State",
        fontsize=11
    )

    plt.tight_layout()

    plt.savefig(
        r"C:\Assignment ACD\DFA\dfa_diagram.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

# MAIN PROGRAM

print("=" * 60)
print("          AUTOMATA THEORY ASSIGNMENT")
print("=" * 60)

print("\nProblem Statement:")
print(problem)

print("Generating DFA diagram...")

create_dfa_diagram()

print("\nDFA diagram created successfully!")

print(
    r"Saved at: C:\Assignment ACD\DFA\dfa_diagram.png"
)