import csv
from pathlib import Path
base=Path(__file__).resolve().parents[1]/'data'
def read(name):
 with (base/name).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
staff=read('contract_staffing_synthetic.csv')
net_hours=sum(float(r['baseline_contractor_hours'])-float(r['illustrative_revised_hours']) for r in staff)
print(f'Fictional 12-week contract-hour difference: {net_hours:.1f} hours; not actual savings')
training=read('training_synthetic.csv'); n=sum(r['assessed']=='1' for r in training);passes=sum(r['passed_if_assessed']=='1' for r in training)
print(f'Fictional competency subset: {passes}/{n} assessed; denominator excludes unassessed')
experience=read('patient_experience_synthetic.csv')
print('Fictional survey observations:',len(experience),'months; not actual patient results')
