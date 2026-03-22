# sample3.py
# Write forecast result to temp file.

import os

OUTPUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','temp','0565_forecast.txt'))


def save_forecast(forecast):
    os.makedirs(os.path.dirname(OUTPUT),exist_ok=True)
    with open(OUTPUT,'w') as f:
        f.write(str(forecast)+'\n')
    return OUTPUT

if __name__=='__main__':
    result={'forecast':16,'mae':1.0}
    path=save_forecast(result)
    print('Saved forecast to',path)
    with open(path) as f:
        print(f.read().strip())
