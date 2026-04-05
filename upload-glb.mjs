import { put } from '@vercel/blob';
import { readFileSync, appendFileSync } from 'fs';

const files = [
  'computer.glb', 'Couch.glb', 'Desk.glb', 'door.glb',
  'egyptian_temple.glb', 'fire.glb', 'floor_lamp.glb', 'garden.glb',
  'hashing.glb', 'heaping.glb', 'linked.glb', 'metal_door.glb',
  'q.glb', 'scifi-room.glb', 'Shelf.glb', 'stack.glb', 'star_wars.glb'
];

for (const file of files) {
  const data = readFileSync(`C:\\Users\\HOME\\escape\\static\\${file}`);
    const blob = await put(file, data, { access: 'private', allowOverwrite: true });
  console.log(`✅ ${file} → ${blob.url}`);
  // saves each URL to a file as it uploads
  appendFileSync('blob-urls.txt', `${file} → ${blob.url}\n`);
}