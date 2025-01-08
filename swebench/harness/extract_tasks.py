import ast
import sys
import json
import os

if __name__ == "__main__":
    source_task_instances = sys.argv[1]
    dest_dir = sys.argv[2]

    with open(source_task_instances) as f:
        task_instances = json.load(f)

    os.makedirs(dest_dir, exist_ok=True)

    for task in task_instances:
        task['patch'] = ast.literal_eval(f'"""{task["patch"]}"""')
        task['test_patch'] = ast.literal_eval(f'"""{task["test_patch"]}"""')
        instance_id = task['instance_id']
        base_commit = task['base_commit']

        instance_path = os.path.join(dest_dir, instance_id)
        os.makedirs(instance_path, exist_ok=True)

        with open(os.path.join(instance_path, 'commit.txt'), 'w') as f:
            f.write(base_commit)

        with open(os.path.join(instance_path, 'gold_patch.patch'), 'w') as f:
            f.write(task['patch'])

        with open(os.path.join(instance_path, 'test_patch.patch'), 'w') as f:
            f.write(task['test_patch'])

        with open(os.path.join(instance_path, 'problem_statement.txt'), 'w') as f:
            f.write(task['problem_statement'])

    
        