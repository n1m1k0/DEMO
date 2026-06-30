# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: FitnessLog
class TagManager:
    def __init__(self, db):
        self.db = db
        self._tags_cache = {}

    def add_tag(self, name):
        if not name.strip(): return False
        with self.db.cursor() as cur:
            try:
                cur.execute("INSERT INTO tags (name) VALUES (%s)", (name,))
                self.db.commit()
                self._tags_cache = {}
                return True
            except Exception as e:
                if "already exists" in str(e).lower():
                    return False
                raise

    def remove_tag(self, name):
        with self.db.cursor() as cur:
            try:
                cur.execute("DELETE FROM tags WHERE name = %s", (name,))
                if cur.rowcount == 0: return False
                self.db.commit()
                self._tags_cache = {}
                return True
            except Exception as e:
                raise

    def add_tag_to_exercise(self, exercise_id, tag_name):
        with self.db.cursor() as cur:
            try:
                cur.execute("INSERT INTO exercise_tags (exercise_id, tag_id) VALUES (%s, %s)",
                            (exercise_id, self._get_or_create_tag(tag_name)))
                self.db.commit()
                return True
            except Exception as e:
                if "already exists" in str(e).lower(): return False
                raise

    def remove_tag_from_exercise(self, exercise_id, tag_name):
        with self.db.cursor() as cur:
            try:
                cur.execute("DELETE FROM exercise_tags WHERE exercise_id = %s AND tag_id = %s",
                            (exercise_id, self._get_or_create_tag(tag_name)))
                if cur.rowcount == 0: return False
                self.db.commit()
                return True
            except Exception as e:
                raise

    def _get_or_create_tag(self, name):
        with self.db.cursor() as cur:
            try:
                cur.execute("SELECT id FROM tags WHERE LOWER(name) = %s", (name.lower(),))
                row = cur.fetchone()
                if row: return row[0]
                cur.execute("INSERT INTO tags (name) VALUES (%s)", (name,))
                self.db.commit()
                self._tags_cache = {}
                return cur.lastrowid
            except Exception as e:
                raise
