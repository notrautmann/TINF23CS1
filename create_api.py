from create_db import get_table_names
def generate():
    
    tables = get_table_names()
    with open("routes.py", "a") as f:
        f.write("import db\n")
        f.write("from flask import request, jsonify\n")

        for table in tables:
            f.write(f"# {table}\n")
            f.write(f"@app.route('/{table}/<int:id>', methods=['GET'])\n")
            f.write(f"def get_{table}(id):\n")
            f.write(f"    # Logic to get {table} data\n")
            f.write(f"    return jsonify(db.{table.capitalize()}.read(id), status=200, mimetype='application/json')\n\n")
            f.write(f"@app.route('/{table}', methods=['POST'])\n")
            f.write(f"def create_{table}():\n")
            f.write(f"    # Logic to create {table} data\n")
            f.write(f"    db.{table.capitalize()}.create(request.values())\n")
            f.write("    return jsonify({'success': True}, status=200, mimetype='application/json')\n\n")
            f.write(f"@app.route('/{table}/<int:id>', methods=['PUT'])\n")
            f.write(f"def update_{table}(id):\n")
            f.write(f"    # Logic to update {table} data\n")
            f.write(f"    db.{table.capitalize()}.update(request.values())\n")
            f.write("    return jsonify({'success': True}, status=200, mimetype='application/json')\n\n")
            f.write(f"@app.route('/{table}/<int:id>', methods=['DELETE'])\n")
            f.write(f"def delete_{table}(id):\n")
            f.write(f"    # Logic to delete {table} data\n")
            f.write(f"    db.{table.capitalize()}.delete(id)\n")
            f.write("    return jsonify({'success': True}, status=200, mimetype='application/json')\n\n")
        f.write("\n")

if __name__ == "__main__":  
    generate()
    print("API routes generated successfully.")
