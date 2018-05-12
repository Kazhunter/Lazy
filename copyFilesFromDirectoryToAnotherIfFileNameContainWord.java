import java.io.*;

public class Main {


    public static void main(String[] args) throws IOException {
        String srcFolder = "/home/kazhunter/Desktop/Courses/Andriod videos/sub";
        String trgFolder = "/home/kazhunter/Desktop/Courses/test";
        String srcFolderNameContains = "_ar_";

        copyFileThatNamesContainToDirectory(srcFolder, trgFolder, srcFolderNameContains);

    }

    private static void copyFileThatNamesContainToDirectory(String srcFolder, String trgFolder, String srcFolderNameContains) throws IOException {
        File folder = new File(srcFolder);
        File[] listOfFiles = folder.listFiles();

        for (int i = 0; i < listOfFiles.length; i++) {
            File file = listOfFiles[i];
            if (file.isFile()) {
                if (file.getName().contains(srcFolderNameContains)) {
                    copyFiles(file, new File(trgFolder));
                }
            }
        }
    }


    private static void copyFiles(File sourceLocation, File targetLocation) throws IOException {

        if (sourceLocation.isFile() && targetLocation.isDirectory()) {

            InputStream in = new FileInputStream(sourceLocation);
            OutputStream out = new FileOutputStream(targetLocation + "/" + sourceLocation.getName());

            // Copy the bits from input stream to output stream
            byte[] buf = new byte[1024];
            int len;
            while ((len = in.read(buf)) > 0) {
                out.write(buf, 0, len);
            }
            in.close();
            out.close();

        }

    }
}
