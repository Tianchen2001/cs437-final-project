import React from 'react';
import './ParkingLot.css';

function ParkingLot() {
    return (
        <div className="parking-lot-container">
            <div className="parking-lot">
                <div className="wall"></div>
                <div className="lane">
                    <div className="parking-row left">
                        {Array.from({ length: 5 }, (_, index) => (
                            <div key={`left-${index}`} className="parking-slot">Slot {index + 1}</div>
                        ))}
                    </div>
                    <div className="parking-row right">
                        {Array.from({ length: 5 }, (_, index) => (
                            <div key={`right-${index}`} className="parking-slot">Slot {index + 6}</div>
                        ))}
                    </div>
                </div>
                <div className="exit"></div>
            </div>
            <div className="message-area">
                Messages go here
            </div>
        </div>
    );
}

export default ParkingLot;
