"use client";

import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

export default function MapWrapper() {
  return (
    <MapContainer center={[51.4613, -0.0767]} zoom={14} style={{ height: 300, width: "100%" }} scrollWheelZoom={false}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution="&copy; OpenStreetMap" />
      <Marker position={[51.4613, -0.0767]}>
        <Popup>East Dulwich Forum HQ</Popup>
      </Marker>
    </MapContainer>
  );
}
