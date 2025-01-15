# Task Tracker

This is a simple task management application where users can add, update, delete, and list tasks via a command-line interface (CLI). The task manager supports both task names and task IDs for various actions.

## Features: - **Add Task:** Create new tasks with descriptions.
- **List Tasks:** Shows all tasks with their creation date, name, description, and status.
- **Delete Task:** You can delete a task by entering either the task name or the task ID.
- **Update Task:** You can change the task name and description by providing the task name or task ID.
- **Mark task status:** You can input the task name or the task ID to mark a task as "todo," "in progress," or "done."


### How to Use:
1. **Running the Program:** 
   - Upon running the program, a menu will appear with the following options:
     ```
     Task Manager
     1. Add Task
     2. List Tasks
     3. Delete Task
     4. Mark Task Status
     5. Update Task
     6. Exit
     ```
2. **Choosing an Option:** - To choose an option from the menu, enter the matching number (1-6):
     You can add a new task by entering its name and description using the - **Add Task (1):** function.
     **List Tasks (2):** Lists all tasks along with their creation date, status, description, and name.
     - **Delete Task (3):** To delete a specific task, enter either its name or ID.
     **Mark Task Status (4):** To modify the task's status (e.g., "todo", "in progress", "done"), enter the task or task ID.
     - **Update Task (5):** Enter either the task name or the task ID to change the task's name and description.
     - **Exit (6):** Quit the program.

For long-term storage, the application automatically saves tasks to a `tasks.json` file.

Project URL:
https://roadmap.sh/projects/task-tracker

