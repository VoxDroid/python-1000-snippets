# sample3.py
# Save supply chain plan to temp.

import os

OUTPUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','temp','0564_supply_chain.txt'))


def save_plan(plan):
    os.makedirs(os.path.dirname(OUTPUT),exist_ok=True)
    with open(OUTPUT,'w') as f:
        f.write(str(plan)+'\n')
    return OUTPUT

if __name__=='__main__':
    plan={'q1':10,'q2':0,'cost':20}
    path=save_plan(plan)
    print('Saved plan to',path)
    with open(path) as f:
        print(f.read().strip())
