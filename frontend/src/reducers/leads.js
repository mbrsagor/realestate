import { GET_LEADS } from ".././actions/types";

const intialState = {
    something: 'text',
    leads: []
};

const leadReducer = (state = intialState, action) => {
  switch (action.type) {
    case GET_LEADS:
      return {
          ...state,
          leads: action.payload
      }
    default: return state
  }
}

export default leadReducer;
