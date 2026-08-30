import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

# PROBLEM STATEMENT

problem = """
Construct an ε-NFA over {0,1} that accepts all strings
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

# DRAW ARROW

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

# CREATE ε-NFA DIAGRAM

def create_nfa_diagram():

    fig, ax = plt.subplots(figsize=(15, 8))

    ax.set_xlim(-2, 12)
    ax.set_ylim(-4, 4)

    ax.axis("off")

    # Title
    ax.text(
        5,
        3.4,
        "ε-NFA",
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
    
    q0 = (0, 0)

    q1 = (3, 2)
    q2 = (6, 2)
    q3 = (9, 2)

    q4 = (3, -2)
    q5 = (6, -2)
    q6 = (9, -2)

    # DRAW STATES
    
    draw_state(ax, *q0, "q0")

    draw_state(ax, *q1, "q1")
    draw_state(ax, *q2, "q2")
    draw_state(ax, *q3, "q3", final=True)

    draw_state(ax, *q4, "q4")
    draw_state(ax, *q5, "q5")
    draw_state(ax, *q6, "q6", final=True)

    # INITIAL STATE
    

    draw_start_arrow(ax, *q0)

    # UPPER PATH: 01

    draw_arrow(
        ax,
        (0.35, 0.25),
        (2.55, 1.75),
        "ε",
        label_offset=(0, 0.15)
    )

    draw_arrow(
        ax,
        (3.45, 2),
        (5.55, 2),
        "0",
        label_offset=(0, 0.25)
    )

    draw_arrow(
        ax,
        (6.45, 2),
        (8.55, 2),
        "1",
        label_offset=(0, 0.25)
    )

    # LOWER PATH: 11

    draw_arrow(
        ax,
        (0.35, -0.25),
        (2.55, -1.75),
        "ε",
        label_offset=(0, -0.15)
    )

    draw_arrow(
        ax,
        (3.45, -2),
        (5.55, -2),
        "1",
        label_offset=(0, -0.25)
    )

    draw_arrow(
        ax,
        (6.45, -2),
        (8.55, -2),
        "1",
        label_offset=(0, -0.25)
    )

    
    # FINAL STATE LOOPS


    draw_self_loop(
        ax,
        *q3,
        "0,1"
    )

    draw_self_loop(
        ax,
        *q6,
        "0,1"
    )


    # LEGEND
    

    ax.text(
        1,
        -3.3,
        "→ Initial State",
        fontsize=11
    )

    ax.text(
        4.5,
        -3.3,
        "Double Circle = Final State",
        fontsize=11
    )

    ax.text(
        8.5,
        -3.3,
        "ε = Epsilon",
        fontsize=11
    )

    plt.tight_layout()

    # Save high-quality image
    plt.savefig(
        r"C:\Assignment ACD\NFA\nfa_diagram.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

# MAIN


print("=" * 60)
print("          AUTOMATA THEORY ASSIGNMENT")
print("=" * 60)

print("\nProblem Statement:")
print(problem)

print("Generating ε-NFA diagram...")

create_nfa_diagram()

print("\nNFA diagram created successfully!")

print(
    r"Saved at: C:\Assignment ACD\NFA\nfa_diagram.png"
)