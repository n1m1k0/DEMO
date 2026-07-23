# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: FitnessLog
import pickle, io, sys, os

def undo_last_action(data: dict) -> None:
    """Откатывает последнее действие в FitnessLog, если оно было."""
    if not data.get('_undo_stack'):
        return
    
    action = data['_undo_stack'].pop()
    if action is None or action == 'no-op':
        return
    
    try:
        if action['type'] == 'add_exercise':
            uid = action['uid']
            for e in data.get('exercises', []):
                if e['id'] == uid:
                    data['exercises'].remove(e)
                    break
        
        elif action['type'] == 'update_set':
            ex_uid, set_data = action['details']
            for e in data.get('exercises', []):
                if e['id'] == ex_uid:
                    sets_idx = next((i for i, s in enumerate(e['sets']) if s is not None), -1)
                    if 0 <= sets_idx < len(e['sets']):
                        e['sets'][sets_idx] = set_data
        
        elif action['type'] == 'delete_exercise':
            uid = action['uid']
            data['exercises'] = [e for e in data.get('exercises', []) if e['id'] != uid]
        
        elif action['type'] == 'update_weight_record':
            record_uid, weight_val = action['details']
            for r in data.get('weight_records', []):
                if r['uid'] == record_uid:
                    r['current'] = weight_val
        
    except Exception as e:
        print(f"Undo failed: {e}", file=sys.stderr)

def main():
    filename = os.path.join(os.path.dirname(__file__) or '.', 'fitness_log.pkl')
    if not os.path.exists(filename):
        print("No save file found. Nothing to undo.")
        return
    
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    
    undo_last_action(data)
    
    buffer = io.BytesIO()
    with open(buffer, 'wb') as f:
        pickle.dump(data, f)
    os.replace(buffer.getvalue(), filename)
    
    print("Last action undone successfully.")

if __name__ == '__main__':
    main()
