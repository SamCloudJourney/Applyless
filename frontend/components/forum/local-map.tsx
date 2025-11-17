"use client";

import dynamic from "next/dynamic";
import { Card, CardContent, CardHeader } from "../ui/card";

const MapContainer = dynamic(() => import("./map-wrapper"), { ssr: false });

export default function LocalMap() {
  return (
    <Card>
      <CardHeader>
        <h3 className="font-semibold">SE22 Activity</h3>
      </CardHeader>
      <CardContent>
        <MapContainer />
      </CardContent>
    </Card>
  );
}
