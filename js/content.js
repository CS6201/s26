/**
 * content.js - Content Loading and Rendering
 * Handles loading and rendering content for each section
 */

// ============================================
// Content Loading
// ============================================

/**
 * Load and render content for a specific section
 * @param {string} sectionId - The ID of the section to load
 */
async function loadSection(sectionId) {
    const mainContent = document.getElementById('main-content');
    
    // Show loading state
    mainContent.innerHTML = '<div class="section"><p>Loading...</p></div>';
    
    try {
        switch(sectionId) {
            case 'about':
                await loadAbout();
                break;
            case 'lectures':
                await loadLectures();
                break;
            case 'labs':
                await loadLabs();
                break;
            case 'assignments':
                await loadAssignments();
                break;
            case 'project':
                await loadProject();
                break;
            case 'examinations':
                await loadExaminations();
                break;
            case 'resources':
                await loadResources();
                break;
            case 'course-policy':
                await loadCoursePolicy();
                break;
            case 'staff':
                await loadStaff();
                break;
            default:
                mainContent.innerHTML = '<div class="section"><h2>Page Not Found</h2><p>The requested page could not be found.</p></div>';
        }
    } catch (error) {
        console.error(`Error loading section ${sectionId}:`, error);
        mainContent.innerHTML = `<div class="section"><h2>Error</h2><p>Failed to load content. Please try again later.</p></div>`;
    }
}

// ============================================
// Section Loaders
// ============================================

/**
 * Load About section
 */
async function loadAbout() {
    const response = await fetch('data/about.md');
    const markdown = await response.text();
    const html = marked.parse(markdown);
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            ${html}
            
            <h3>Graded Components</h3>
            <table>
                <thead>
                    <tr>
                        <th>Component</th>
                        <th>Weightage (%)</th>
                        <th>Details</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Quizzes</td>
                        <td>10</td>
                        <td>Two quizzes: 5% each</td>
                    </tr>
                    <tr>
                        <td>Paper Exams</td>
                        <td>30</td>
                        <td>Mid-semester and End-semester: 15% each</td>
                    </tr>
                    <tr>
                        <td>Lab Exams</td>
                        <td>30</td>
                        <td>Mid-semester and End-semester: 15% each</td>
                    </tr>
                    <tr>
                        <td>Programming Assignments</td>
                        <td>10</td>
                        <td>Assignment 1 and 2: 5% each</td>
                    </tr>
                    <tr>
                        <td>Lab Submissions & Paper Assignments</td>
                        <td>10</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Project</td>
                        <td>10</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td><strong>Total</strong></td>
                        <td><strong>100</strong></td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            
            <div class="note">
                <strong>Note:</strong> The course instructors reserve the right to make modifications to the above distribution based on the progress of the course.
            </div>
        </div>
    `;
}

/**
 * Load Lectures section
 */
async function loadLectures() {
    const response = await fetch('data/lectures.json');
    const data = await response.json();
    
    let lectureRows = '';
    data.lectures.forEach(lecture => {
        lectureRows += `
            <tr>
                <td>${lecture.number}</td>
                <td>${lecture.sectionA || ''}</td>
                <td>${lecture.sectionB || ''}</td>
                <td>${lecture.topic || ''}</td>
                <td>${lecture.slides ? `<a href="${lecture.slides}" target="_blank">Slides</a>` : ''}</td>
                <td>${lecture.references ? `<a href="${lecture.references}" target="_blank">References</a>` : ''}</td>
            </tr>
        `;
    });
    
    let tutorialRows = '';
    if (data.tutorials && data.tutorials.length > 0) {
        data.tutorials.forEach(tutorial => {
            tutorialRows += `
                <tr>
                    <td>${tutorial.number}</td>
                    <td>${tutorial.date || ''}</td>
                    <td>${tutorial.date || ''}</td>
                    <td>${tutorial.topic || ''}</td>
                    <td>${tutorial.slides ? `<a href="${tutorial.slides}" target="_blank">Slides</a>` : ''}</td>
                    <td>${tutorial.references ? `<a href="${tutorial.references}" target="_blank">References</a>` : ''}</td>
                </tr>
            `;
        });
    }
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Lectures</h2>
            <div class="section-info">
                <p><strong>Timing:</strong> 8:30 - 9:55</p>
                <p><strong>Section A:</strong> SH-1</p>
                <p><strong>Section B:</strong> SH-2</p>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Lecture Number</th>
                        <th>Section A</th>
                        <th>Section B</th>
                        <th>Topic</th>
                        <th>Slides</th>
                        <th>References</th>
                    </tr>
                </thead>
                <tbody>
                    ${lectureRows}
                </tbody>
            </table>
            
            <h3>Tutorials</h3>
            <div class="section-info">
                <p><strong>Timing:</strong> 8:30 - 9:55</p>
                <p><strong>Section A:</strong> SH-1</p>
                <p><strong>Section B:</strong> SH-2</p>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Tutorial Number</th>
                        <th>Section A</th>
                        <th>Section B</th>
                        <th>Topic</th>
                        <th>Slides</th>
                        <th>References</th>
                    </tr>
                </thead>
                <tbody>
                    ${tutorialRows}
                </tbody>
            </table>
        </div>
    `;
}

/**
 * Load Labs section
 */
async function loadLabs() {
    const response = await fetch('data/labs.json');
    const data = await response.json();
    
    let tableRows = '';
    data.labs.forEach(lab => {
        tableRows += `
            <tr>
                <td>${lab.number}</td>
                <td>${lab.date || ''}</td>
                <td>${lab.topic || ''}</td>
                <td>${lab.slides ? `<a href="${lab.slides}" target="_blank">Slides</a>` : ''}</td>
                <td>${lab.activity ? `<a href="${lab.activity}" download>Activity</a>` : ''}</td>
                <td>${lab.references ? `<a href="${lab.references}" target="_blank">References</a>` : ''}</td>
            </tr>
        `;
    });
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Labs</h2>
            <div class="section-info">
                <p><strong>Timing:</strong> 14:00 - 17:00</p>
                <p><strong>Location:</strong> H-105</p>
                <p><strong>Note:</strong> Laptops are required for all lab sessions.</p>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Lab Number</th>
                        <th>Date</th>
                        <th>Topic</th>
                        <th>Slides</th>
                        <th>Activity</th>
                        <th>References</th>
                    </tr>
                </thead>
                <tbody>
                    ${tableRows}
                </tbody>
            </table>
        </div>
    `;
}

/**
 * Load Assignments section
 */
async function loadAssignments() {
    const response = await fetch('data/assignments.json');
    const data = await response.json();
    
    let tableRows = '';
    data.assignments.forEach(assignment => {
        tableRows += `
            <tr>
                <td>${assignment.number}</td>
                <td>${assignment.topic || ''}</td>
                <td>${assignment.announcement || ''}</td>
                <td>${assignment.deadline || ''}</td>
                <td>${assignment.link ? `<a href="${assignment.link}" target="_blank">Link</a>` : ''}</td>
            </tr>
        `;
    });
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Assignments</h2>
            <div class="section-info">
                <p><strong>Note:</strong> All submissions will be made through GitHub Classroom or HackerRank.</p>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Assignment Number</th>
                        <th>Topic</th>
                        <th>Announcement</th>
                        <th>Deadline</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    ${tableRows}
                </tbody>
            </table>
        </div>
    `;
}

/**
 * Load Project section
 */
async function loadProject() {
    const response = await fetch('data/project.md');
    const markdown = await response.text();
    const html = marked.parse(markdown);
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Project</h2>
            ${html}
        </div>
    `;
}

/**
 * Load Examinations section
 */
async function loadExaminations() {
    const response = await fetch('data/examinations.json');
    const data = await response.json();
    
    let tableRows = '';
    data.examinations.forEach(exam => {
        tableRows += `
            <tr>
                <td>${exam.serial}</td>
                <td>${exam.type || ''}</td>
                <td>${exam.start || ''}</td>
                <td>${exam.end || ''}</td>
                <td>${exam.link ? `<a href="${exam.link}" target="_blank">Link</a>` : ''}</td>
            </tr>
        `;
    });
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Examinations</h2>
            
            <table>
                <thead>
                    <tr>
                        <th>Serial Number</th>
                        <th>Exam Type</th>
                        <th>Start Time</th>
                        <th>End Time</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    ${tableRows}
                </tbody>
            </table>
            
            <div class="note">
                <strong>Note:</strong> More examinations may be added as the semester progresses. This is not the final schedule.
            </div>
        </div>
    `;
}

/**
 * Load Resources section
 */
async function loadResources() {
    const response = await fetch('data/resources.json');
    const data = await response.json();
    
    let tableRows = '';
    data.resources.forEach(resource => {
        tableRows += `
            <tr>
                <td>${resource.serial}</td>
                <td>${resource.type || ''}</td>
                <td>${resource.title || ''}</td>
                <td>${resource.link ? `<a href="${resource.link}" target="_blank">Link</a>` : ''}</td>
            </tr>
        `;
    });
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Resources</h2>
            
            <table>
                <thead>
                    <tr>
                        <th>Serial Number</th>
                        <th>Resource Type</th>
                        <th>Title</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    ${tableRows}
                </tbody>
            </table>
        </div>
    `;
}

/**
 * Load Course Policy section
 */
async function loadCoursePolicy() {
    const response = await fetch('data/policy.md');
    const markdown = await response.text();
    const html = marked.parse(markdown);
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Course Policy</h2>
            ${html}
        </div>
    `;
}

/**
 * Load Staff section
 */
async function loadStaff() {
    const response = await fetch('data/staff.json');
    const data = await response.json();
    
    // Generate instructor cards
    let instructorCards = '';
    data.instructors.forEach(instructor => {
        instructorCards += `
            <div class="staff-card">
                ${instructor.photo 
                    ? `<img src="${instructor.photo}" alt="${instructor.name}" class="staff-photo">` 
                    : `<div class="staff-photo placeholder">👤</div>`
                }
                <h3>${instructor.name}</h3>
                <p><strong>Email:</strong> <a href="mailto:${instructor.email}">${instructor.email}</a></p>
                ${instructor.website ? `<p><strong>Website:</strong> <a href="https://${instructor.website}" target="_blank">${instructor.website}</a></p>` : ''}
                ${instructor.researchLab ? `<p><strong>Research Lab:</strong> ${instructor.researchLab}</p>` : ''}
            </div>
        `;
    });
    
    // Generate TA cards
    let taCards = '';
    data.tas.forEach(ta => {
        taCards += `
            <div class="staff-card">
                ${ta.photo 
                    ? `<img src="${ta.photo}" alt="${ta.name}" class="staff-photo">` 
                    : `<div class="staff-photo placeholder">👤</div>`
                }
                <h3>${ta.name}</h3>
                <p><strong>Email:</strong> <a href="mailto:${ta.email}">${ta.email}</a></p>
                ${ta.hours ? `<p><strong>TA Hours:</strong> ${ta.hours}</p>` : ''}
                ${ta.location ? `<p><strong>Location:</strong> ${ta.location}</p>` : ''}
            </div>
        `;
    });
    
    document.getElementById('main-content').innerHTML = `
        <div class="section">
            <h2>Course Staff</h2>
            
            <div class="staff-container">
                <h3>Instructors</h3>
                <div class="staff-grid">
                    ${instructorCards}
                </div>
            </div>
            
            <div class="staff-container">
                <h3>Teaching Assistants</h3>
                <div class="staff-grid">
                    ${taCards}
                </div>
            </div>
            
            <div class="staff-note">
                <strong>Note:</strong> Please email a TA at least 24 hours before showing up to their office hours.
            </div>
        </div>
    `;
}
