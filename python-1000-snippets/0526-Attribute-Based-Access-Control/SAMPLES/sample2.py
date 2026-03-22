# sample2.py
# Evaluate and print policy results for multiple subjects.


def evaluate_subjects(subjects, resource):
    return {s['id']: (s['dept'] == resource['department'] and s['clearance'] >= resource['required_clearance'])
            for s in subjects}


if __name__ == '__main__':
    subjects = [{'id': 1, 'dept': 'IT', 'clearance': 3}, {'id': 2, 'dept': 'HR', 'clearance': 5}]
    resource = {'department': 'IT', 'required_clearance': 2}
    print('Policy results:', evaluate_subjects(subjects, resource))
