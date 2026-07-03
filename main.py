from tests.test_cases import run_tests
from analysis.run_analysis import run_analysis

from visualization.plot_ph import plot_ph
from visualization.plot_SpO2 import plot_spo2
from report.generate_report import generate_report

def main():
    print("\n===================================")
    print("  BIOMEDICAL DECISION SYSTEM")
    print("===================================\n")

    print("[1] Running Tests...")
    run_tests()

    print("\n[2] Running Analysis...")
    run_analysis()

    print("\n[3] Generating Plots...")
    plot_ph()
    plot_spo2()

    print("\n[4] Generating PDF Report...")
    generate_report()

    print("\n===================================")
    print(" SYSTEM COMPLETE ")
    print("===================================\n")


if __name__ == "__main__":
    main()