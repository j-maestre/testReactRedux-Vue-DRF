import { userApi } from "../../api";

const state = {
  token: {},
  loading: false,
  user: {},
};

const mutations = {
  LOGIN(state, payload) {
    state.token = payload;
  },
  SET_LOADER(state, payload) {
    state.loading = payload;
  },
  SET_USER(state, payload) {
    state.user = payload;
  },
};

const actions = {
  login({ commit }, credentials) {
    commit("SET_LOADER", true);

    userApi
      .login(credentials)
      .then(() => {
        commit("SET_LOADER", false);
        commit("SET_MSG", {
          type: true,
          title: "Authentication success",
          details: "The login was successful",
        });
      })
      .catch(() =>
        commit("SET_MSG", {
          type: false,
          title: "Authentication failed",
          details: "The login was completed incorrectly",
        })
      );

    commit("LOGIN", credentials);
  },
};

const getters = {};

export default { state, mutations, getters, actions };