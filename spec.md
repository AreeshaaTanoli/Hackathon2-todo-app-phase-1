# Phase I – In-Memory Todo Application Specification

## Overview
A Python console-based Todo application that manages tasks during runtime using in-memory storage.

## Data Model
Each task includes:
- id (integer, auto-increment)
- title (string)
- completed (boolean)

## Functional Requirements

### Add Task
- User enters a task title
- Task is stored in memory
- Default completed status is false

### View Tasks
- Display all tasks
- Show ID, title, and status

### Update Task
- Update task title using task ID

### Delete Task
- Remove task using task ID

### Mark Task as Complete
- Toggle completed status by task ID

## Interface
- Menu-driven console interface
- Runs until user chooses exit

## Error Handling
- Invalid IDs handled gracefully
