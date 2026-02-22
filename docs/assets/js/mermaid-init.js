// Initialize Mermaid after the library is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (typeof mermaid !== 'undefined') {
        mermaid.initialize({
            startOnLoad: false,
            theme: 'default'
        });
        mermaid.run({
            querySelector: '.mermaid'
        });
    }
});
