import React, { useState } from 'react';
import './ParkingLot.css';

function ParkingLot() {
    const [message, setMessage] = useState('Message will appear here');

    const handleSlotClick = (slotNumber) => {
        setMessage(`Car is moving to slot ${slotNumber}`);
    };

    const handleExitClick = () => {
        setMessage('Car is exiting the parking lot');
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
                        {Array.from({ length: 5 }, (_, index) => (
                            <div key={`left-${index}`} className="parking-slot" onClick={() => handleSlotClick(index + 1)}>
                                Slot {index + 1}
                            </div>
                        ))}
                    </div>
                    <div className="parking-row right">
                        {Array.from({ length: 5 }, (_, index) => (
                            <div key={`right-${index}`} className="parking-slot" onClick={() => handleSlotClick(index + 6)}>
                                Slot {index + 6}
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
