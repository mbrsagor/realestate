import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getLeads } from '../../actions/leadsAction';


class Leads extends Component {

    static propTypes = {
        leads: PropTypes.array.isRequired
    }

    componentDidMount() {
        this.props.getLeads()
    }

    render() {
        return (
            <div>
                <h3>Lead Lists</h3>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    leads: state.leadReducer.leads
})

export default connect(mapStateToProps, {getLeads}) (Leads) 
