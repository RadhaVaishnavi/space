const imageInput = document.getElementById('image-input');
const captionOutput = document.getElementById('caption-output');
const loadingIndicator = document.getElementById('loading-indicator');

imageInput.addEventListener('change', async () => {
  const file = imageInput.files[0];
  const formData = new FormData();
  formData.append('image', file);

  loadingIndicator.style.display = 'block'; // Show loading indicator
  captionOutput.textContent = ''; // Clear previous caption

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    captionOutput.textContent = data.caption;
  } catch (error) {
    console.error(error);
    captionOutput.textContent = 'Error generating caption.';
  } finally {
    loadingIndicator.style.display = 'none'; // Hide loading indicator
  }
});
