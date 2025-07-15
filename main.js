// Main JavaScript file for Hindalco Digital Culture Pledge

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize form validation
    initializeFormValidation();
    
    // Initialize survey form enhancements
    initializeSurveyForm();
    
    // Initialize admin dashboard
    initializeAdminDashboard();
});

// Form validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        });
    });
}

// Survey form enhancements
function initializeSurveyForm() {
    const surveyForm = document.getElementById('surveyForm');
    if (!surveyForm) return;
    
    // Add progress tracking
    const sections = surveyForm.querySelectorAll('.section-header');
    const progressBar = createProgressBar(sections.length);
    
    if (sections.length > 0) {
        sections[0].parentNode.insertBefore(progressBar, sections[0]);
    }
    
    // Track form completion
    trackFormCompletion();
    
    // Add auto-save functionality
    addAutoSave();
}

// Create progress bar
function createProgressBar(totalSections) {
    const progressContainer = document.createElement('div');
    progressContainer.className = 'progress-container mb-4';
    progressContainer.innerHTML = `
        <div class="progress" style="height: 8px;">
            <div class="progress-bar" role="progressbar" style="width: 0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small class="text-muted">Form Progress: <span id="progress-text">0%</span></small>
    `;
    
    return progressContainer;
}

// Track form completion
function trackFormCompletion() {
    const formInputs = document.querySelectorAll('#surveyForm input, #surveyForm textarea, #surveyForm select');
    const progressBar = document.querySelector('.progress-bar');
    const progressText = document.getElementById('progress-text');
    
    if (!progressBar || !progressText) return;
    
    function updateProgress() {
        const totalFields = formInputs.length;
        let completedFields = 0;
        
        formInputs.forEach(input => {
            if (input.value.trim() !== '') {
                completedFields++;
            }
        });
        
        const percentage = Math.round((completedFields / totalFields) * 100);
        progressBar.style.width = percentage + '%';
        progressBar.setAttribute('aria-valuenow', percentage);
        progressText.textContent = percentage + '%';
    }
    
    formInputs.forEach(input => {
        input.addEventListener('input', updateProgress);
        input.addEventListener('change', updateProgress);
    });
    
    // Initial update
    updateProgress();
}

// Auto-save functionality
function addAutoSave() {
    const surveyForm = document.getElementById('surveyForm');
    if (!surveyForm) return;
    
    let autoSaveTimeout;
    const autoSaveDelay = 5000; // 5 seconds
    
    function saveFormData() {
        const formData = new FormData(surveyForm);
        const dataObject = {};
        
        formData.forEach((value, key) => {
            dataObject[key] = value;
        });
        
        localStorage.setItem('survey_draft', JSON.stringify(dataObject));
        showAutoSaveNotification();
    }
    
    function showAutoSaveNotification() {
        const notification = document.createElement('div');
        notification.className = 'alert alert-success alert-dismissible fade show position-fixed';
        notification.style.cssText = 'top: 20px; right: 20px; z-index: 1050; width: 300px;';
        notification.innerHTML = `
            <i class="fas fa-save me-2"></i>
            Form auto-saved
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
    
    // Load saved data on page load
    const savedData = localStorage.getItem('survey_draft');
    if (savedData) {
        try {
            const dataObject = JSON.parse(savedData);
            Object.keys(dataObject).forEach(key => {
                const input = surveyForm.querySelector(`[name="${key}"]`);
                if (input) {
                    input.value = dataObject[key];
                }
            });
        } catch (e) {
            console.error('Error loading saved form data:', e);
        }
    }
    
    // Auto-save on form changes
    surveyForm.addEventListener('input', function() {
        clearTimeout(autoSaveTimeout);
        autoSaveTimeout = setTimeout(saveFormData, autoSaveDelay);
    });
    
    // Clear saved data on successful submission
    surveyForm.addEventListener('submit', function() {
        localStorage.removeItem('survey_draft');
    });
}

// Admin dashboard initialization
function initializeAdminDashboard() {
    const exportButton = document.querySelector('[href*="export_data"]');
    if (exportButton) {
        exportButton.addEventListener('click', function(e) {
            e.preventDefault();
            
            const button = this;
            const originalText = button.innerHTML;
            
            button.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Exporting...';
            button.disabled = true;
            
            // Simulate export process
            setTimeout(() => {
                window.location.href = button.href;
                
                setTimeout(() => {
                    button.innerHTML = originalText;
                    button.disabled = false;
                }, 2000);
            }, 1000);
        });
    }
}

// Utility functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 1050; width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export functions for global use
window.HindalcoApp = {
    showNotification,
    formatDate,
    debounce
};
