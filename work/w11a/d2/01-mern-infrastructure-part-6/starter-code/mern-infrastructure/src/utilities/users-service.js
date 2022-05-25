import * as usersAPI from './users-api';

export async function signUp(userData) {
  // Delegate the network request code to the users-api.js
  // module which will ultimately return a JWT
  const token = await usersAPI.signUp(userData);
  return token;
}