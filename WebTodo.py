import streamlit as st
import functions

# Initialize todos
todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

# Initialize session state
if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""

st.title("WebTodoGUI")
st.subheader("This is my Todo app.")

# Display todos with unique keys
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

st.info("Created by: Aryan Kumar Upadhyay")
