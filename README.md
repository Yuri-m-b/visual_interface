# Visual Interface

A small Python GUI application built with PySide6 and Qt that displays a romantic multi-screen visual interface. The app uses a `QStackedWidget` to switch between several custom page widgets, each rendered with images, text, and interactive buttons.

## Features

- Multi-page Qt interface using `QStackedWidget`
- Custom page widgets derived from `QWidget`
- Image-based buttons and screen flow
- Clickable answers and interactive UI behavior
- Wrong answer buttons can disappear when clicked
- Animated screen transitions using `QTimer`
- Layouts mixed with absolute button positioning for a custom visual experience

## Qt Library Used

This project uses `PySide6`, the official Python bindings for Qt 6.

Key Qt components used:

- `QApplication` - application object and event loop
- `QMainWindow` - main window container
- `QStackedWidget` - stack of pages for navigation
- `QWidget` - base class for custom pages
- `QLabel` - image and text display
- `QPushButton` - interactive buttons
- `QVBoxLayout` - basic vertical layout for page content
- `QPixmap` - image loading
- `QTimer` - delayed actions and timed behavior

## Implementation Overview

The interface is implemented in `interface/interface.py`.

### MainWindow

`MainWindow` creates the application window and hosts a `QStackedWidget`. It instantiates ten page widgets and adds them to the stack.

### Page classes

The app uses page classes such as:

- `FirstPage` - welcome screen with a start button
- `SecondPage` - yes/no question where the "No" button moves randomly
- `ThirdPage` - image selection screen
- `FourthPage` - a page with multiple clickable image buttons
- `FifthPage` - answer screen with wrong options that disappear when clicked
- `SixthPage` through `TenthPage` - additional screens with image buttons and final content

Each page class sets up its UI in `init_ui()` and uses signals like `clicked.connect(...)` to change the currently displayed page.

### Wrong answer behavior

Wrong answer buttons are handled in `FifthPage` by connecting buttons to a lambda that calls `fail_attempt()`. If the user clicks a wrong button, the button is removed from the interface with `deleteLater()`.

## Running the Project

1. Install dependencies:

```bash
pip install PySide6
```

2. Run the application:

```bash
python3 interface/interface.py
```

3. Make sure the `images/` folder is present and contains the image files referenced in `FIGURE_MAPPING`.

## Project Structure

- `interface/interface.py` - main application code
- `interface/interface.css` - application stylesheet loaded at runtime
- `images/` - image assets used by the UI
- `README.md` - project documentation

## Notes

- The UI uses a combination of layouts and explicit widget positioning.
- `interface/interface.css` provides the app-wide styling applied to the `QApplication`.
- The app is designed as a personalized visual experience and demonstrates simple Qt navigation patterns.
