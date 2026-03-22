# sample1.py
# ABAC policy decision based on attributes.


def can_access(user_attrs, resource_attrs):
    return (user_attrs.get('department') == resource_attrs.get('department')
            and user_attrs.get('clearance', 0) >= resource_attrs.get('required_clearance', 0))


if __name__ == '__main__':
    user = {'department': 'IT', 'clearance': 5}
    resource = {'department': 'IT', 'required_clearance': 4}
    print('Access', can_access(user, resource))
