import streamlit as st
import functions

todos_filepath = "todos.txt"
todos = functions.get_todos(todos_filepath)


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos, todos_filepath)


st.title('My todo app')
st.subheader('This is my todo app')
st.write('This app is to increase my productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, todos_filepath)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
