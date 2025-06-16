from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.obj import EventLog
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter as pt_converter
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualizer

# --- STEP 1: Load the XES event log ---
log = xes_importer.apply("./DataSet/BPI Challenge 2017.xes")
print(" Log loaded")

# --- STEP 2: Sort all events in each trace by timestamp ---
for trace in log:
    trace[:] = sorted(trace, key=lambda x: x["time:timestamp"])

print(" Events sorted by timestamp")

# --- STEP 3: Remove traces with fewer than 2 events (can't compute directly-follows relationships) ---
log = EventLog([trace for trace in log if len(trace) >= 2])
print(f" Traces with ≥2 events: {len(log)}")

# --- STEP 4: Discover Petri net using Inductive Miner ---
process_tree = inductive_miner.apply(log)
net, initial_marking, final_marking = pt_converter.apply(process_tree)

# --- STEP 5: Save Petri net visualization ---
pn_gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.save(pn_gviz, "Output/petri_net_inductive.png")
print(" Petri net saved as 'petri_net_inductive.png'")

# --- STEP 6: Try to generate performance-based DFG ---
dfg_perf = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)

# --- STEP 7: Visualize the DFG (fallback to frequency if needed) ---
if not dfg_perf:
    print(" Performance DFG was empty — falling back to frequency DFG.")
    dfg_freq = dfg_discovery.apply(log, variant=dfg_discovery.Variants.FREQUENCY)

    if not dfg_freq:
        print(" Frequency DFG also empty — no valid sequences found.")
    else:
        dfg_gviz = dfg_visualizer.apply(dfg_freq, log=log, variant=dfg_visualizer.Variants.FREQUENCY)
        dfg_visualizer.save(dfg_gviz, "dfg_frequency.png")
        print(" Frequency DFG saved as 'dfg_frequency.png'")
else:
    dfg_gviz = dfg_visualizer.apply(dfg_perf, log=log, variant=dfg_visualizer.Variants.PERFORMANCE)
    dfg_visualizer.save(dfg_gviz, "Output/dfg_performance.png")
    print(" Performance DFG saved as 'dfg_performance.png'")
