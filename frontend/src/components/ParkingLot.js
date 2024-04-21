import React, { useState } from 'react';
import axios from 'axios';
import './ParkingLot.css';

function ParkingLot() {
    const [message, setMessage] = useState('Message will appear here');

    const baseURL = 'http://192.168.88.220:5000';

    const handleSlotClick = (slotNumber) => {
        setMessage(`Car is moving to slot ${slotNumber}`);
        axios.post(`${baseURL}/move`, { slot: slotNumber })
            .then(response => {
                console.log(response.data);
                setMessage(`Response: ${response.data.message}`);
            })
            .catch(error => {
                console.error('Error:', error);
                setMessage(`Error: ${error.message}`);
            });
    };

    const handleExitClick = () => {
        setMessage('Car is exiting the parking lot');
        axios.post(`${baseURL}/exit`, { action: 'exit' })
            .then(response => {
                console.log(response.data);
                setMessage(`Response: ${response.data.message}`);
            })
            .catch(error => {
                console.error('Error:', error);
                setMessage(`Error: ${error.message}`);
            });
    };

    return (
        <div className="parking-lot-container">
            <div className="parking-lot-title">
                Interactive Parking Lot Layout
            </div>
            <div className="parking-lot">
                <div className="wall"></div>
                <div className="lane">
                    <div className="parking-row left">
                        {Array.from({ length: 4 }, (_, index) => (
                            <div key={`left-${index}`} className="parking-slot" onClick={() => handleSlotClick(index + 1)}>
                                Slot {index + 1}
                            </div>
                        ))}
                    </div>
                    <div className="parking-row right">
                        {Array.from({ length: 4 }, (_, index) => (
                            <div key={`right-${index}`} className="parking-slot" onClick={() => handleSlotClick(index + 5)}>
                                Slot {index + 5}
                            </div>
                        ))}
                    </div>
                </div>
                <div className="exit" onClick={handleExitClick}>Exit</div>
            </div>
            <div className="message-box">
                {message}
            </div>
        </div>
    );
}

export default ParkingLot;
