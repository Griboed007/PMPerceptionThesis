from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.visualization.bpmn import visualizer as bpmn_visualizer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter as pt_converter
from pm4py.objects.log.obj import EventLog

# --- STEP 1: Load XES log ---
log = xes_importer.apply('./DataSet/BPI Challenge 2017.xes')
print("✅ Log loaded")

# --- STEP 2: Sort events by timestamp in each trace ---
for trace in log:
    trace[:] = sorted(trace, key=lambda x: x["time:timestamp"])
print("✅ Events sorted")

# --- STEP 3: Filter traces with <2 events ---
log = EventLog([trace for trace in log if len(trace) >= 2])
print(f"✅ Filtered traces: {len(log)}")

# --- STEP 4: Discover ProcessTree using Inductive Miner ---
process_tree = inductive_miner.apply(log, variant=inductive_miner.Variants.IMf)
print("✅ ProcessTree discovered")

# --- STEP 5: Convert ProcessTree to BPMN ---
bpmn_model = pt_converter.apply(process_tree, variant=pt_converter.Variants.TO_BPMN)
print("✅ Converted ProcessTree to BPMN")

# --- STEP 6: Visualize and save the BPMN diagram ---
gviz = bpmn_visualizer.apply(bpmn_model)
bpmn_visualizer.save(gviz, "Output/bpmn_model.png")
print("✅ BPMN model saved as 'bpmn_model.png'")
