/**
 * WonderBees Services — API layer (ES modules).
 * Legacy pages load js/bootstrap.js (type=module) to attach window.WonderbeeServicesAPI.
 */

export const API_CONFIG = {
  contact: "/api/contact",
  formspree: "https://formspree.io/f/YOUR_FORM_ID",
  /** reCAPTCHA v3 site key — https://www.google.com/recaptcha/admin — replace to show badge & verify contact form */
  recaptchaSiteKey: "YOUR_RECAPTCHA_V3_SITE_KEY",
};

/**
 * Future backend JSON contact endpoint.
 * @param {Record<string, unknown>} data
 * @returns {Promise<Response>}
 */
export async function submitForm(data) {
  return fetch(API_CONFIG.contact, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}

/**
 * @param {FormData} formData
 * @returns {Promise<Response>}
 */
export function submitContactViaFormspree(formData) {
  return fetch(API_CONFIG.formspree, {
    method: "POST",
    body: formData,
    headers: { Accept: "application/json" },
  });
}
