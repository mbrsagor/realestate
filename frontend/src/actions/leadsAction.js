import axios from 'axios';
import { GET_LEADS } from './types';


// get leads 
export const getLeads = () =>  dispatch =>{
    axios.get("http://127.0.0.1:8000/api/leads/")
        .then(res => {
            dispatch({
                type: GET_LEADS,
                payload: res.data
            })
        }).catch(error => console.log(error));
}
