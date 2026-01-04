# Introduction to Software Systems - Course Website

A modular course website for "Introduction to Software Systems" (Spring 2026) at International Institute of Information Technology, Hyderabad.

## Features

- **Dark/Light Theme Toggle**: Persistent theme preference saved in browser localStorage
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modular Architecture**: Easy to add, edit, or remove content
- **Static Website**: No server-side processing required - can be hosted anywhere
- **Clean Navigation**: Sticky navbar with 9 main sections
- **Markdown Support**: Content can be written in Markdown for easy formatting

## File Structure

```
Course Website/
├── index.html              # Main HTML file
├── css/
│   └── styles.css         # All styling with dark/light theme support
├── js/
│   ├── main.js            # Theme toggle and navigation logic
│   └── content.js         # Content loading and rendering
└── data/                  # All content files (edit these to update website)
    ├── about.md           # About section content
    ├── lectures.json      # Lectures data
    ├── labs.json          # Labs data
    ├── assignments.json   # Assignments data
    ├── project.md         # Project information
    ├── examinations.json  # Examinations data
    ├── resources.json     # Resources list
    ├── policy.md          # Course policy
    └── staff.json         # Staff information (instructors and TAs)
```

## How to Use

### 1. Viewing the Website

**IMPORTANT**: Due to browser security restrictions (CORS), you cannot simply open `index.html` directly. You need to run a local web server.

#### Option A: Using Python (Recommended)

Run the included server script:

```bash
python server.py
```

This will automatically start a server at `http://localhost:8000` and open your browser.

#### Option B: Using Python's built-in server

```bash
# Python 3
python -m http.server 8000

# Then open browser to: http://localhost:8000
```

#### Option C: Using VS Code Live Server Extension

1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

#### For Deployment

Upload all files to any static web hosting service (GitHub Pages, Netlify, Vercel, etc.). Once deployed, the website will work without any server setup.

### 2. Editing Content

All content is stored in the `data/` folder. Edit these files to update the website:

#### Markdown Files (.md)

Used for sections with rich text content:

- `about.md` - Course overview and description
- `project.md` - Project information
- `policy.md` - Course policies

**How to edit**: Write plain text or use Markdown formatting:

```markdown
# Heading 1
## Heading 2
**bold text**
*italic text*
- Bullet point
1. Numbered list
[Link text](URL)
```

#### JSON Files (.json)

Used for tabular data. Follow the existing structure:

**lectures.json** - Add/edit lecture entries:

```json
{
  "lectures": [
    {
      "number": 1,
      "sectionA": "Jan 15, 2026",
      "sectionB": "Jan 16, 2026",
      "topic": "Introduction to Software Systems",
      "slides": "path/to/slides.pdf",
      "references": "path/to/references.pdf"
    }
  ]
}
```

**labs.json** - Add/edit lab entries:

```json
{
  "labs": [
    {
      "number": 1,
      "date": "Jan 20, 2026",
      "topic": "BASH Shell Basics",
      "slides": "path/to/slides.pdf",
      "references": "path/to/references.pdf"
    }
  ]
}
```

**assignments.json** - Add/edit assignment entries:

```json
{
  "assignments": [
    {
      "number": 1,
      "topic": "Shell Scripting",
      "announcement": "Jan 15, 2026- 10:00",
      "deadline": "Jan 30, 2026- 23:59",
      "github": "https://classroom.github.com/..."
    }
  ]
}
```

**examinations.json** - Add/edit exam entries:

```json
{
  "examinations": [
    {
      "serial": 1,
      "type": "Quiz 1",
      "topic": "OS Basics",
      "announcement": "Feb 1, 2026- 10:00",
      "deadline": "Feb 15, 2026- 17:00",
      "github": "https://classroom.github.com/..."
    }
  ]
}
```

**resources.json** - Add/edit resource entries:

```json
{
  "resources": [
    {
      "serial": 1,
      "type": "Book",
      "title": "Operating System Concepts",
      "link": "https://example.com/book"
    }
  ]
}
```

**staff.json** - Add/edit instructor and TA information:

```json
{
  "instructors": [
    {
      "name": "Dr. John Doe",
      "email": "john.doe@iiit.ac.in",
      "photo": "images/john-doe.jpg",
      "website": "https://example.com/johndoe",
      "hours": "Monday 14:00 - 16:00",
      "location": "Room 301, Academic Block"
    }
  ],
  "tas": [
    {
      "name": "Jane Smith",
      "email": "jane.smith@iiit.ac.in",
      "photo": "images/jane-smith.jpg",
      "hours": "Tuesday 15:00 - 17:00",
      "location": "TA Room, Lab Building"
    }
  ]
}
```

### 3. Adding Images

1. Create an `images/` folder in the root directory
2. Add your image files (photos, logos, etc.)
3. Reference them in JSON files using relative paths: `"images/photo.jpg"`

### 4. Customizing Styles

Edit `css/styles.css` to customize colors, fonts, and layout:

**Changing Theme Colors**:

```css
:root {
    /* Dark theme colors */
    --bg-primary: #1a1a1a;      /* Main background */
    --accent-primary: #4a9eff;   /* Links and accents */
    /* ... edit other variables ... */
}

body.light-theme {
    /* Light theme colors */
    --bg-primary: #ffffff;
    --accent-primary: #0066cc;
    /* ... edit other variables ... */
}
```

### 5. Adding a New Section

To add a completely new section:

1. **Add navigation link** in `index.html`:

   ```html
   <li><a href="#new-section" class="nav-link">New Section</a></li>
   ```

2. **Create data file** in `data/` folder (e.g., `new-section.md` or `new-section.json`)

3. **Add loader function** in `js/content.js`:

   ```javascript
   async function loadNewSection() {
       const response = await fetch('data/new-section.md');
       const markdown = await response.text();
       const html = marked.parse(markdown);
       
       document.getElementById('main-content').innerHTML = `
           <div class="section">
               <h2>New Section</h2>
               ${html}
           </div>
       `;
   }
   ```

4. **Add case** in `loadSection()` function:

   ```javascript
   case 'new-section':
       await loadNewSection();
       break;
   ```

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Dependencies

- **Marked.js** (v11.0.0+): For Markdown parsing
  - Loaded from CDN in `index.html`
  - No installation required

## Tips for Maintenance

1. **Regular Backups**: Keep backups of the `data/` folder before major updates
2. **Testing**: After editing, always test in a browser before deploying
3. **Validation**: Use online JSON validators to check JSON file syntax
4. **Images**: Optimize images before adding (use JPEG for photos, PNG for graphics)
5. **Links**: Use absolute URLs for external resources, relative paths for local files

## Troubleshooting

**Problem**: "Failed to load content" error

- **Solution**: You must run a local web server. Do NOT open `index.html` directly. Use `python server.py` or one of the other methods listed above.

**Problem**: Content not loading after running server

- **Solution**: Check browser console (F12) for errors. Verify JSON syntax is correct.

**Problem**: Theme not persisting

- **Solution**: Ensure browser allows localStorage. Check browser settings.

**Problem**: Broken links

- **Solution**: Verify all file paths are correct and files exist.

**Problem**: Markdown not rendering

- **Solution**: Verify Marked.js CDN link is accessible. Check network connection.

## Support

For questions or issues with the website structure, refer to:

- HTML/CSS/JavaScript documentation
- Markdown guide: <https://www.markdownguide.org/>
- JSON format guide: <https://www.json.org/>

---

**Last Updated**: January 2026  
**Version**: 1.0
