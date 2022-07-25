from rss_main import main

if __name__ == '__main__':
    print(
        main('tests/assets/trabalho4/netlist0.txt', 1e-3, 0.2e-3, 1e-4,
             [1, 0.5], [1, 2]))
