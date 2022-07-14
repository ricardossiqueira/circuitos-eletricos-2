from src.app.rss_main import main as app_main


def main(netlist_file, sim_uptime, nr_step, nr_lim, initial_values,
         target_nodes):
    return app_main(netlist_file, sim_uptime, nr_step, nr_lim, initial_values,
                    target_nodes)
