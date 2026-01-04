/**
 * main.js - Theme Toggle and Navigation Management
 * Handles dark/light theme switching and navigation between sections
 */

// ============================================
// Theme Management
// ============================================

/**
 * Initialize theme based on user's saved preference or default to dark theme
 */
function initializeTheme() {
    // Check if user has a saved theme preference
    const savedTheme = localStorage.getItem('theme');
    const themeToggle = document.getElementById('theme-toggle');
    
    if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
        themeToggle.querySelector('.theme-icon').textContent = '🌙';
    } else {
        // Default to dark theme
        themeToggle.querySelector('.theme-icon').textContent = '☀️';
    }
}

/**
 * Toggle between dark and light themes
 */
function toggleTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('.theme-icon');
    
    body.classList.toggle('light-theme');
    
    // Update icon and save preference
    if (body.classList.contains('light-theme')) {
        themeIcon.textContent = '🌙';
        localStorage.setItem('theme', 'light');
    } else {
        themeIcon.textContent = '☀️';
        localStorage.setItem('theme', 'dark');
    }
}

// ============================================
// Navigation Management
// ============================================

/**
 * Toggle sidebar navigation
 */
function toggleNav() {
    const navbar = document.getElementById('navbar');
    const overlay = document.getElementById('nav-overlay');
    const body = document.body;
    
    navbar.classList.toggle('open');
    overlay.classList.toggle('active');
    body.classList.toggle('nav-open');
}

/**
 * Close sidebar navigation
 */
function closeNav() {
    const navbar = document.getElementById('navbar');
    const overlay = document.getElementById('nav-overlay');
    const body = document.body;
    
    navbar.classList.remove('open');
    overlay.classList.remove('active');
    body.classList.remove('nav-open');
}

/**
 * Update active navigation link based on current section
 * @param {string} sectionId - The ID of the current section
 */
function updateActiveNav(sectionId) {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href').substring(1); // Remove '#'
        
        if (href === sectionId) {
            link.classList.add('active');
        }
    });
}

/**
 * Handle navigation clicks and load appropriate content
 * @param {Event} e - Click event
 */
function handleNavigation(e) {
    e.preventDefault();
    const targetId = e.target.getAttribute('href').substring(1); // Remove '#'
    
    // Close navigation sidebar
    closeNav();
    
    // Update URL hash without jumping
    history.pushState(null, null, `#${targetId}`);
    
    // Update active navigation
    updateActiveNav(targetId);
    
    // Load content for the section
    loadSection(targetId);
    
    // Scroll to top of main content
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

/**
 * Initialize navigation event listeners
 */
function initializeNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', handleNavigation);
    });
    
    // Handle browser back/forward buttons
    window.addEventListener('popstate', () => {
        const hash = window.location.hash.substring(1) || 'about';
        updateActiveNav(hash);
        loadSection(hash);
    });
    
    // Load initial section based on URL hash or default to 'about'
    const initialSection = window.location.hash.substring(1) || 'about';
    updateActiveNav(initialSection);
    loadSection(initialSection);
}

// ============================================
// Event Listeners
// ============================================

/**
 * Initialize all event listeners when DOM is loaded
 */
document.addEventListener('DOMContentLoaded', () => {
    // Initialize theme
    initializeTheme();
    
    // Add theme toggle listener
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.addEventListener('click', toggleTheme);
    
    // Add navigation toggle listener
    const navToggle = document.getElementById('nav-toggle');
    navToggle.addEventListener('click', toggleNav);
    
    // Add overlay click listener to close nav
    const overlay = document.getElementById('nav-overlay');
    overlay.addEventListener('click', closeNav);
    
    // Initialize navigation
    initializeNavigation();
});
