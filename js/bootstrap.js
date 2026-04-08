/**
 * Attaches WonderbeeServicesAPI (legacy JS global name) for classic scripts (main.js) on pages that import this module first.
 */
import { API_CONFIG, submitForm, submitContactViaFormspree } from "./api.js";

window.WonderbeeServicesAPI = {
  API_CONFIG,
  submitContactToBackend: submitForm,
  submitContactViaFormspree,
  submitForm,
};
