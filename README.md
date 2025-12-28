# To-Do App with Reminders & Notifications

A modern, responsive web-based to-do application with reminder functionality and browser notifications built with Flask and vanilla JavaScript.

## Features

- ✅ Add, **edit**, and delete tasks
- 🔔 Set reminders with date and time
- 📬 **Browser notifications at reminder time**
- ✏️ **Edit tasks after creation** (change title, description, time)
- ✨ Mark tasks as complete/incomplete
- 🎯 Filter tasks (All, Active, Completed)
- ⚠️ Visual indicators for overdue tasks
- 💾 Persistent data storage
- 📱 Responsive design for mobile and desktop

## New Features

### Edit Tasks
- Click the "✏️ Edit" button on any task
- Modify task title, description, or reminder time
- Changes are saved instantly

### Browser Notifications
- Enable notifications when prompted
- Get automatic browser notifications when reminder time arrives
- Notifications appear even when tab is in background
- Checks for reminders every 30 seconds
- Marks tasks as notified to avoid duplicate notifications

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd todo-app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

6. **Allow browser notifications** when prompted to receive reminders

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Notifications**: Browser Notification API
- **Storage**: JSON file (easily upgradeable to database)
- **Server**: Gunicorn (production)

## How It Works

### Notifications System
1. App requests notification permission on first load
2. Background checker runs every 30 seconds
3. When a reminder time is reached (within 1 minute), notification fires
4. Task is marked as "notified" to prevent duplicate alerts
5. Clicking notification brings app window to focus

### Edit Functionality
1. Click "Edit" button on any task
2. Modal popup with current task details
3. Modify any field (title, description, reminder)
4. Submit to save changes
5. Notification flag resets if reminder time changes

## Browser Compatibility

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support (macOS/iOS)
- Opera: Full support

**Note**: Notifications require HTTPS in production

## Future Enhancements

- [ ] User authentication
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Email/SMS notifications for reminders
- [ ] Task categories and tags
- [ ] Dark mode
- [ ] Task sharing and collaboration
- [ ] Recurring tasks
- [ ] Mobile app (React Native)
- [ ] Priority levels
- [ ] Task search and sorting

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Support

For issues or questions, please open an issue on GitHub.
